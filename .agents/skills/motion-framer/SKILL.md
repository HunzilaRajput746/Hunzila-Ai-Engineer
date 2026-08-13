---
name: motion-framer
description: "Expert knowledge of Motion for React (formerly Framer Motion) — the production-grade React animation library. Use when implementing animations, transitions, gestures, scroll effects, layout animations, or any motion-related UI in React/Next.js projects. Covers motion component, AnimatePresence, useScroll, useSpring, useTransform, whileHover, whileTap, variants, keyframes, stagger, and more."
---

# Motion for React (Framer Motion) — Animation Reference

> **Package**: `motion` (formerly `framer-motion`)
> **Import**: `import { motion } from "motion/react"`
> **Install**: `npm install motion`

Motion for React is the successor to Framer Motion. It uses a hybrid engine — Web Animations API + ScrollTimeline for 120fps hardware-accelerated performance, falling back to JavaScript for springs, interruptible keyframes, and gesture tracking.

---

## Core Concepts

### The `<motion />` Component
Prefix any HTML/SVG element with `motion.` to unlock animation props:

```jsx
import { motion } from "motion/react"

// Basic animate prop
<motion.div animate={{ opacity: 1, x: 100 }} />

// With transition
<motion.div
  animate={{ scale: 2 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
/>
```

### Key Props
| Prop | Description |
|------|-------------|
| `animate` | Target animation state |
| `initial` | Starting state (or `false` to skip enter animation) |
| `exit` | State when component is removed (needs `AnimatePresence`) |
| `transition` | Controls duration, delay, easing, type (spring/tween) |
| `whileHover` | Animation while hovered |
| `whileTap` | Animation while tapped/clicked |
| `whileFocus` | Animation while focused |
| `whileDrag` | Animation while dragged |
| `whileInView` | Animation while in viewport |
| `variants` | Named animation states for orchestration |
| `layout` | Enables smooth layout animations |
| `drag` | Enables drag gesture (`true`, `"x"`, `"y"`) |

---

## Enter & Exit Animations

```jsx
// Enter animation
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.4, ease: "easeOut" }}
/>

// Exit animation
import { motion, AnimatePresence } from "motion/react"

<AnimatePresence>
  {isVisible && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.2 }}
    />
  )}
</AnimatePresence>
```

---

## Gestures

```jsx
<motion.button
  whileHover={{ scale: 1.05, y: -2 }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
/>

<motion.div
  drag
  dragConstraints={{ left: -100, right: 100, top: -50, bottom: 50 }}
  dragElastic={0.2}
  whileDrag={{ scale: 1.05 }}
/>
```

---

## Variants (Stagger Orchestration)

```jsx
const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: { staggerChildren: 0.1, delayChildren: 0.3 }
  }
}
const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
}

<motion.ul variants={container} initial="hidden" animate="show">
  {items.map(i => <motion.li key={i} variants={item} />)}
</motion.ul>
```

---

## Transitions

```jsx
// Spring (best for interactive)
transition={{ type: "spring", stiffness: 300, damping: 20 }}

// Tween
transition={{ type: "tween", duration: 0.4, ease: "easeInOut" }}

// Keyframes
animate={{ x: [0, 100, 0] }}
transition={{ duration: 1, times: [0, 0.5, 1] }}

// Loop
animate={{ rotate: 360 }}
transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
```

---

## Scroll Animations

```jsx
import { useScroll, useTransform, useSpring } from "motion/react"

function ParallaxSection() {
  const { scrollYProgress } = useScroll()
  const y = useTransform(scrollYProgress, [0, 1], ["0%", "50%"])
  return <motion.div style={{ y }} />
}

// whileInView
<motion.div
  initial={{ opacity: 0, y: 60 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ once: true, margin: "-100px" }}
  transition={{ duration: 0.6 }}
/>
```

---

## Motion Values

```jsx
import { useMotionValue, useTransform, useSpring, useMotionTemplate } from "motion/react"

const x = useMotionValue(0)
const opacity = useTransform(x, [-200, 0, 200], [0, 1, 0])
const smoothX = useSpring(x, { stiffness: 300, damping: 30 })
const background = useMotionTemplate`hsl(${hue}deg, 100%, 50%)`
```

---

## Common Patterns

### Floating animation
```jsx
<motion.div
  animate={{ y: [0, -15, 0] }}
  transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
/>
```

### Card hover
```jsx
<motion.div
  whileHover={{ y: -8, boxShadow: "0 20px 40px rgba(0,0,0,0.3)" }}
  transition={{ type: "spring", stiffness: 400, damping: 25 }}
/>
```

### Magnetic button
```jsx
function MagneticButton({ children }) {
  const x = useMotionValue(0)
  const y = useMotionValue(0)
  return (
    <motion.button
      style={{ x, y }}
      onMouseMove={(e) => {
        const rect = e.currentTarget.getBoundingClientRect()
        x.set((e.clientX - rect.left - rect.width / 2) * 0.3)
        y.set((e.clientY - rect.top - rect.height / 2) * 0.3)
      }}
      onMouseLeave={() => { x.set(0); y.set(0) }}
      transition={{ type: "spring", stiffness: 300 }}
    >
      {children}
    </motion.button>
  )
}
```

---

## Best Practices

1. Prefer GPU-accelerated props: `x`, `y`, `scale`, `rotate`, `opacity`
2. Avoid animating `width`/`height` directly — use `scaleX`/`scaleY` or `layout`
3. Use `viewport={{ once: true }}` for one-time scroll animations
4. Spring: interactive elements | Tween: UI transitions
5. Respect `useReducedMotion()` for accessibility
6. Duration: micro=100-200ms, UI=200-400ms, page=300-500ms
7. Stagger children: 0.05–0.15s per item
