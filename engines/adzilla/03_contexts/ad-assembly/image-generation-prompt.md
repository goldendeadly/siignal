# Advanced Image Generation Prompt — AdZilla v2.0

> Integrated from the Universal Image Creation Meta-Prompt. This prompt is triggered during the `ad-assembly` context to generate AI-ready image prompts for every ad creative.

---

## Purpose

When AdZilla assembles final ad creatives, this module generates **production-ready image prompts** for AI image generators (DALL-E, Midjourney, Flux, Stable Diffusion). Each prompt is structured to produce high-converting visual assets that match the campaign's tone, avatar psychology, and platform requirements.

---

## Image Prompt Framework

For every ad creative generated, produce an accompanying image prompt using the following 7-layer structure:

### Layer 1: Purpose and Context
- **Objective:** What is the image for? (e.g., Facebook ad, Instagram story, landing page hero)
- **Audience:** Which avatar is this targeting? (Pull from Avatar Intelligence Core)
- **Emotional Target:** What feeling should the viewer experience in the first 0.5 seconds?

### Layer 2: Subject and Composition
- **Primary Focus:** Who or what is the central subject?
- **Key Objects/Symbols:** What must be included to communicate the offer?
- **Setting/Environment:** What backdrop reinforces the message?
- **Perspective:** Close-up, wide-angle, bird's-eye, eye-level?
- **Balance:** Rule of thirds, symmetry, dynamic diagonal?

### Layer 3: Style and Tone
- **Artistic Style:** Hyperrealistic, cinematic, minimalistic, editorial, abstract?
- **Cultural/Genre Influence:** Modern corporate, luxury, street-level, aspirational lifestyle?
- **Tone:** Warm/inviting, cold/moody, bold/energetic, calm/trustworthy?

### Layer 4: Lighting and Color
- **Lighting Type:** Natural daylight, studio, dramatic chiaroscuro, neon, golden hour?
- **Direction/Intensity:** Backlit, diffused, high contrast, soft fill?
- **Primary Palette:** Aligned with brand colors and avatar psychology
- **Accent Colors:** For contrast, highlights, or CTA emphasis
- **Texture:** Metallic, matte, glossy, organic?

### Layer 5: Textures and Details
- **Material Emphasis:** Glossy surfaces, rough textures, fabric, glass, concrete?
- **Detail Level:** Highly intricate or clean and simplified?
- **Specific Details:** "The shimmer on a glass surface" or "minimal shadows on flat planes"

### Layer 6: Symbolism and Messaging
- **Symbolic Elements:** Motifs that reinforce the transformation promise
- **Text Overlay Zones:** Where should text be placed? (Leave negative space)
- **Brand Anchors:** Logo placement, color consistency, visual identity markers

### Layer 7: Technical Specifications
- **Aspect Ratio:** 1:1 (Instagram), 9:16 (Stories/Reels), 16:9 (YouTube), 4:5 (Facebook)
- **Resolution:** High-res (1024x1024 minimum)
- **Format Notes:** PNG for transparency, JPG for web delivery
- **Platform Constraints:** Text-to-image ratio limits (Meta 20% rule)

---

## Output Format

For each ad creative, generate:

```
IMAGE PROMPT [Platform] — [Avatar Name]
---
Style: [artistic style]
Subject: [primary focus description]
Setting: [environment/backdrop]
Lighting: [type and direction]
Colors: [primary palette + accents]
Mood: [emotional tone]
Composition: [perspective + balance]
Aspect Ratio: [ratio]
Negative Space: [where text can be overlaid]
---
Full Prompt: "[Complete, detailed prompt ready for AI image generator]"
```

---

## Integration Rules

1. **Every ad variant** produced in ad-assembly MUST include a corresponding image prompt.
2. **Avatar alignment** — The visual style must match the avatar's psychological profile (e.g., "The Status Seeker" gets luxury aesthetics; "The Logical Operator" gets clean, data-driven visuals).
3. **Platform optimization** — Each platform gets its own aspect ratio and style adaptation.
4. **A/B Visual Testing** — Generate 2 image prompt variants per ad (one "safe," one "bold") for split testing.
