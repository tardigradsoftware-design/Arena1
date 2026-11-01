#!/usr/bin/env bash
# Restore the checked-in preferred VID-035 ingredients into the working layout.
# This overwrites working images and voice.wav: use only when regenerating 035.
set -euo pipefail
root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
src="$root/reference/VID-035"
mkdir -p "$root/images" "$root/audio" "$root/remotion/public"
cp "$src"/images/*.png "$root/images/"
cp "$src"/images/*.png "$root/remotion/public/"
cp "$src"/audio/VID-035.wav "$src"/audio/VID-035-fast.wav "$root/audio/"
cp "$src/audio/VID-035-fast.wav" "$root/remotion/public/voice.wav"
cp "$root/assets/peaceful_days.mp3" "$root/assets/whoosh.wav" "$root/assets/drip.wav" "$root/remotion/public/"
mkdir -p "$root/videos"
echo "VID-035 kaynakları hazır; senaryo ve zamanlamaları render öncesi kontrol edin."
