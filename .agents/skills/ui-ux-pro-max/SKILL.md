---
name: ui-ux-pro-max
description: "UI/UX design intelligence for web and mobile. Includes 84 styles, 192 color palettes, 74 font pairings, 98 UX guidelines, 16 GSAP motion presets, and 25 chart types. Use when designing, building, or reviewing UI: pages, components, color schemes, typography, layout, accessibility, animation, or data visualization."
---

# UI/UX Pro Max — Design Intelligence

## When to Apply
Use when task involves: UI structure, visual design decisions, interaction patterns, or UX quality.

Skip for: pure backend logic, API/database design, non-visual performance, infrastructure.

---

## Rule Categories by Priority

| Priority | Category | Impact | Key Checks |
|----------|----------|--------|-----------|
| 1 | **Accessibility** | CRITICAL | Contrast 4.5:1, Alt text, Keyboard nav, Aria-labels |
| 2 | **Touch & Interaction** | CRITICAL | Min 44×44px targets, 8px+ spacing, Loading feedback |
| 3 | **Performance** | HIGH | WebP/AVIF, Lazy loading, CLS < 0.1 |
| 4 | **Style Selection** | HIGH | Match product type, SVG icons (no emoji as icons) |
| 5 | **Layout & Responsive** | HIGH | Mobile-first, No horizontal scroll |
| 6 | **Typography & Color** | MEDIUM | Base 16px, Line-height 1.5, Semantic color tokens |
| 7 | **Animation** | MEDIUM | 150–300ms duration, conveys meaning, reduced-motion support |
| 8 | **Forms & Feedback** | MEDIUM | Visible labels, Error near field |
| 9 | **Navigation** | HIGH | Predictable back, Bottom nav ≤5 |
| 10 | **Charts & Data** | LOW | Legends, Tooltips, Accessible colors |

---

## Animation Guidelines (Priority 7)

### Do
- Duration: **150–300ms** for micro-interactions, **200–500ms** for transitions
- Use motion to convey **meaning** (spatial continuity, cause & effect)
- Provide **spatial continuity** — elements move from where they were
- Support `prefers-reduced-motion` media query
- Use **easing**: `ease-out` for enter, `ease-in` for exit, `ease-in-out` for transforms

### Don't
- Don't animate for decoration only (no value, just distraction)
- Don't animate `width`/`height` (layout thrashing) — use `transform: scaleX/scaleY`
- Don't ignore `prefers-reduced-motion`
- Don't use animations > 500ms for UI feedback
- Don't use linear easing for UI (feels robotic)

### Motion Presets (GSAP-style, applicable to any library)
| Preset | Use Case | Duration | Easing |
|--------|----------|----------|--------|
| fadeIn | Page sections, modals | 400ms | ease-out |
| slideUp | Cards, list items | 350ms | cubic-bezier(0.22,1,0.36,1) |
| scaleIn | Buttons, badges | 200ms | spring(stiffness=400) |
| stagger | List reveals | 80ms/child | ease-out |
| float | Hero elements | 3000ms | ease-in-out, infinite |
| parallax | Background layers | scroll-driven | linear |
| magneticHover | CTA buttons | 200ms | spring |
| pageTransition | Route changes | 300ms | ease-in-out |

---

## Color Palette Recommendations

### Dark Mode (Premium)
- Background: `oklch(0.12 0.01 260)` or `hsl(222, 47%, 7%)`
- Surface: `oklch(0.16 0.015 260)` or `hsl(222, 35%, 12%)`
- Border: `oklch(0.25 0.02 260)` or `rgba(255,255,255,0.08)`
- Text: `oklch(0.92 0.008 260)` or `hsl(210, 40%, 92%)`
- Accent: vibrant, e.g. `oklch(0.7 0.2 250)` (purple), `oklch(0.75 0.18 140)` (green)

### Glassmorphism
```css
background: rgba(255, 255, 255, 0.05);
backdrop-filter: blur(16px) saturate(180%);
border: 1px solid rgba(255, 255, 255, 0.1);
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
```

---

## Typography System

### Font Pairing (Modern)
| Role | Font | Weight |
|------|------|--------|
| Display | Clash Display / Cal Sans | 700 |
| Heading | Inter / Plus Jakarta Sans | 600-700 |
| Body | Inter / DM Sans | 400-500 |
| Mono | JetBrains Mono / Fira Code | 400 |

### Scale (rem-based)
```css
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px - minimum body */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 1.875rem;  /* 30px */
--text-4xl: 2.25rem;   /* 36px */
--text-5xl: 3rem;      /* 48px */
```

---

## Spacing System (8px base)
```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-6: 24px;
--space-8: 32px;
--space-12: 48px;
--space-16: 64px;
--space-24: 96px;
```

---

## Interaction Patterns

### Button States
```css
/* Default → Hover → Active → Disabled */
button { transition: all 200ms ease; }
button:hover { transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,0,0,0.3); }
button:active { transform: translateY(0); }
button:disabled { opacity: 0.4; cursor: not-allowed; }
```

### Card Hover
```css
.card {
  transition: transform 300ms cubic-bezier(0.22,1,0.36,1), box-shadow 300ms ease;
}
.card:hover {
  transform: translateY(-8px);
  box-shadow: 0 24px 48px rgba(0,0,0,0.4);
}
```

---

## Anti-Patterns to Avoid

- ❌ Mixing flat and skeuomorphic styles randomly
- ❌ Using emoji as icons in UI
- ❌ Text smaller than 12px
- ❌ Gray-on-gray (insufficient contrast)
- ❌ Raw hex colors in components (use tokens)
- ❌ Placeholder-only labels on inputs
- ❌ Decorative-only animations with no semantic meaning
- ❌ Animating `width`/`height` (use `transform` instead)
- ❌ No `prefers-reduced-motion` support
- ❌ Removing focus rings (destroys keyboard accessibility)
- ❌ Icon-only buttons without aria-labels
