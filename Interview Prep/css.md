# CSS Study Guide

## 1. Selectors and Specificity

### CSS Selectors:
* Target elements based on their type, class, ID, attributes, etc.

### Example:
```
p { color: blue; } /* Type selector */
.class { color: red; } /* Class selector */
#id { color: green; } /* ID selector */
```

### Specificity:
* Determines which CSS rule is applied when multiple rules match an element.
* Inline styles > IDs > Classes > Elements.

## 2. Box Model

### CSS Box Model:
* Describes the layout of elements: content, padding, border, and margin.

#### Example:
```
div {
  width: 100px;
  padding: 10px;
  border: 5px solid black;
  margin: 20px;
}
```

### Changing Box Model Behavior:
* Use box-sizing: border-box; to include padding and border in the element's width and height.

## 3. Layout and Flexbox/Grid

### Flexbox:
* One-dimensional layout system for aligning items in a row or column.

#### Example:
```
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

### Grid:
* Two-dimensional layout system for creating complex layouts.

#### Example:
```
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
}
```

### Flexbox vs. Grid:
* Use Flexbox for simpler, one-dimensional layouts.
* Use Grid for more complex, two-dimensional layouts.

## 4. Responsive Design

### Making a Website Responsive:
* Use relative units like %, em, and rem.
* Use flexible layouts (e.g., Flexbox, Grid).

### Media Queries:
* Apply styles based on screen size or device type.

#### Example:
```
@media (max-width: 600px) {
  body {
    font-size: 14px;
  }
}
```