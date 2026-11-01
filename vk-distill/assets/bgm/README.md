# BGM slot
Standing rule: every Vibe知识大赏 voiceover runs over **"we never"** under 云希.
Drop the file here as `we-never.mp3` (path set in `bases/*/style-base.yaml → bgm.path`; per-episode override `beats.yaml meta.bgm`).
Swap = one re-mux, no re-render (picture is cached at `build/render/picture_douyin.mp4`, muxed with `-c:v copy`):

    cd episodes/<ep> && python3 ../../tools/mix_export.py . build/render/<ep>_raw.mp4 "out/<title>_douyin_1080p30.mp4"

Mix rules: start_s → loop/trim to video → fade in 0.8 s / out 1.8 s → level-matched so the bed sits −20 LU under the voice
while it speaks (QA band −22…−18, measured on the ducked stem in speech windows) → sidechain ducked, lifts in pauses.
Result + which file was actually used: `qa/mix_report.json`. Missing file → synth bed, `fallback_synth: true`.
Note: WaveBars are driven by build/music/music_env.json (synth motif); with a real track they keep the synth envelope
unless you re-run synth_music/env extraction + re-render.

## Current file (2026-10-30)
we-never.mp3 = "We Never (Remix) (若如初见)" — Hi Noise / 秋成 (Douyin/汽水: "We Never(若如初见)Vibe版" by 秋成, song id 7696709382423562291).
Source: YouTube https://www.youtube.com/watch?v=v75KA9sbk2U ("Vibe知识大赏 BGM：We Never (Remix) (若如初见)-Hi Noise/秋成", fan re-upload by "Pad Music Team", 2026-10-23), yt-dlp, 189.9 s, 48 kHz stereo.
License: NOT a free/official release — copyrighted; personal edit only. For publishing, attach the song in Douyin's own music picker instead.
Tempo ≈ 112 BPM (librosa), first beat ≈ 0.44 s, beat ≈ 0.534 s.
