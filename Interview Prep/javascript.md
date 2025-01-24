<style>
r { color: Red }
o { color: Orange }
g { color: Green }
</style>

# JavaScript Study Guide

## 1. Fundamentals

### Difference between var, let, and const:

<r>var</r>: Function-scoped, can be redeclared, and hoisted with undefined initialization.

<r>let</r>: Block-scoped, cannot be redeclared, and hoisted without initialization.

<r>const</r>: Block-scoped, cannot be redeclared or reassigned, and hoisted without initialization.

### Closures:

* A closure is a function that retains access to its outer scope, even after the outer function has executed.

#### Example:

```
function outer() {
  let count = 0;
  return function inner() {
    count++;
    return count;
  };
}
const counter = outer();
console.log(counter()); // 1
console.log(counter()); // 2
```

### Prototypal Inheritance:

* Objects in JavaScript can inherit properties and methods from other objects via the prototype chain.

#### Example:
```
function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {
  return `Hello, ${this.name}`;
};
const john = new Person('John');
console.log(john.greet()); // Hello, John
```

## 2. ES6+ Features

### Arrow Functions:
* Shorter syntax for functions.
* Do not have their own this or arguments object.

#### Example:
```
const add = (a, b) => a + b;
console.log(add(2, 3)); // 5
```

### Async and Await:
* Simplify working with promises by allowing asynchronous code to look synchronous.

#### Example:
```
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
```

## 3. DOM Manipulation

### Adding Event Listeners:

#### Example:
```
document.getElementById('btn').addEventListener('click', () => {
  console.log('Button clicked!');
});
```

### Event Delegation:
* Attaching a single event listener to a parent element to handle events for its child elements.

#### Example:
```
document.getElementById('parent').addEventListener('click', (event) => {
  if (event.target.tagName === 'BUTTON') {
    console.log('Button clicked:', event.target.textContent);
  }
});
```

## 4. Asynchronous JavaScript

### Promises:
* Represent the eventual completion (or failure) of an asynchronous operation.

#### Example:
```
const promise = new Promise((resolve, reject) => {
  setTimeout(() => resolve('Success!'), 1000);
});
promise.then((result) => console.log(result));
```

### Fetch:
* Used to make HTTP requests.

#### Example:
```
fetch('https://api.example.com/data')
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

## 5. Error Handling

### try...catch:
* Used to handle errors gracefully.

#### Example:
```
try {
  const result = riskyOperation();
  console.log(result);
} catch (error) {
  console.error('An error occurred:', error.message);
}
```