"""Fail-closed review gate; this does not detect visual defects on its own."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path


class QualityError(ValueError):
    pass


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def validate(review_path: Path, images: list[Path]) -> None:
    """Require a fresh, explicit visual review for every actual image."""
    if not images:
        raise QualityError('no images supplied')
    try:
        data = json.loads(review_path.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise QualityError(f'review unavailable or invalid: {review_path}: {exc}') from exc
    entries = data.get('images') if isinstance(data, dict) else None
    if not isinstance(entries, list):
        raise QualityError('images must be a list')
    indexed = {}
    for entry in entries:
        if not isinstance(entry, dict) or not isinstance(entry.get('file'), str):
            raise QualityError('invalid image review entry')
        path = (review_path.parent / entry['file']).resolve()
        if path in indexed:
            raise QualityError(f'duplicate review: {path}')
        indexed[path] = entry
    expected = [Path(p).resolve() for p in images]
    if len(set(expected)) != len(expected):
        raise QualityError('duplicate requested image')
    for path in expected:
        e = indexed.get(path)
        if e is None:
            raise QualityError(f'unreviewed: {path}')
        if not path.is_file():
            raise QualityError(f'image missing: {path}')
        if e.get('sha256') != digest(path):
            raise QualityError(f'image changed since review: {path}')
        score = e.get('score')
        if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
            raise QualityError(f'invalid score: {path}')
        if e.get('reviewed') is not True or e.get('critical_error') is not False:
            raise QualityError(f'not reviewed or critical defect: {path}')
        if not isinstance(e.get('notes'), str) or not e['notes'].strip():
            raise QualityError(f'review notes required: {path}')
        if score < 90:
            raise QualityError(f'not approved (score {score}): {path}')


def decision(score: int, critical_error: bool, retries: int) -> str:
    """Return an action, not an automated image-model call. 0 means first output."""
    if isinstance(score, bool) or not isinstance(score, int) or not 0 <= score <= 100:
        raise ValueError('score must be 0..100')
    if not isinstance(critical_error, bool) or isinstance(retries, bool) or not isinstance(retries, int) or not 0 <= retries <= 3:
        raise ValueError('invalid critical_error or retries')
    if score >= 90 and not critical_error:
        return 'accept'
    return 'regenerate' if retries < 3 else 'simplify_composition'
