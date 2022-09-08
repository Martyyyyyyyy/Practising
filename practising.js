function checkGmail() {
    let emailvalidation = document.getElementById('email').value;
    if (emailvalidation.length < 12) {
      document.getElementById('site-heading').style.color = "red";
    } else if (emailvalidation.indexOf('@gmail.com') == -1) {
      document.getElementById('site-heading').style.color = "red";
    } else if (emailvalidation.indexOf('.') < emailvalidation.length - 4) {
  
      document.getElementById('site-heading').style.color = "red";
    } else {
      document.getElementById('site-heading').style.color = "green";
    }
  }

function errorHandler(err) {
    if (typeof err === 'error') {
    throw err;
    }
    else {
        console.error('Unexpectedly, no error was passed to error handler. But here is the message:',err);
    }
}
  
var myError = new Error('foo');
myError instanceof Error // true
var myString = "Whatever";
myString instanceof Error // false

let isError = (e) => {
    return e && e.stack && e.message && typeof e.stack === 'string' 
           && typeof e.message === 'string';
}

function isError(obj){
    return Object.prototype.toString.call(obj) === "[object Error]";
}

function isError(obj){
    return Object.prototype.toString.call(obj) === "[object Error]";
}
console.log("Error:", isError(new Error));
console.log("RangeError:", isError(new RangeError));
console.log("SyntaxError:", isError(new SyntaxError));
console.log("Object:", isError({}));
console.log("Array:", isError([]));

try {
    myRoutine();
  } catch (e) {
    if (e instanceof RangeError) {
      // statements to handle this very common expected error
    } else {
      throw e;  // re-throw the error unchanged
    }
  }

var error = new Error("ValidationError");
console.log(error.constructor.name);

function _err(type = false) {
    if(type) {
        throw new TypeError('Oh crap!')
    }
    throw new Error('Oh crap!')
}

try {
    _err(true)
} catch (error) {
    console.log(typeof error.name, error.name, error.name === 'TypeError')
}

try {
    _err()
} catch (error) {
    console.log(typeof error.name, error.name, error.name === 'Error')
}

const groceryList = ['orange juice', 'bananas', 'coffee beans', 'brown rice', 'pasta', 'coconut oil', 'plantains'];

groceryList.shift();

console.log(groceryList);

groceryList.unshift('popcorn');

console.log(groceryList);

console.log(groceryList.slice(1, 4));

console.log(groceryList);

const pastaIndex = groceryList.indexOf('pasta');

console.log(pastaIndex);

//nested for loops
const bobsFollowers = ['Martin', 'Max', 'John', 'Cambell'];
const tinasFollowers = ['Martin', 'Max', 'Judith'];
const mutualFollowers = [];
for (let i = 0; i < bobsFollowers.length; i++) {
  for (let j = 0; j < tinasFollowers.length; j++) {
    if (bobsFollowers[i] === tinasFollowers[j]) {
      mutualFollowers.push(bobsFollowers[i]);
    }
  }
}
// do while loop
let cupsOfSugarNeeded = 23;
let cupsAdded = 0;
do {
 cupsAdded++
 console.log(cupsAdded + ' cup was added') 
} while (cupsAdded < cupsOfSugarNeeded);
// break keyword
for (let i = 0; i < rapperArray.length; i++){
    console.log(rapperArray[i]);
    if (rapperArray[i] === 'Notorious B.I.G.'){
      break;
    }
  }
  
  console.log("And if you don't know, now you know.");