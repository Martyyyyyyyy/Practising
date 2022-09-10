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

//Nested for loops
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

// Do while loop
let cupsOfSugarNeeded = 23;
let cupsAdded = 0;
do {
 cupsAdded++
 console.log(cupsAdded + ' cup was added') 
} while (cupsAdded < cupsOfSugarNeeded);

// Break keyword
for (let i = 0; i < rapperArray.length; i++){
    console.log(rapperArray[i]);
    if (rapperArray[i] === 'Notorious B.I.G.'){
      break;
    }
  }
  
  console.log("And if you don't know, now you know.");

// Higher-order functions 
const addTwo = num => {
  return num + 2;
}
  
const checkConsistentOutput = (func, val) => {
  const checkA = val + 2;
  const checkB = func(val);
  if (checkA === checkB) {
    return checkB;
  } else {
    console.log('inconsistent results');
  }
}
  
console.log(checkConsistentOutput(addTwo, 5));

// Iterators
const artists = ['Picasso', 'Kahlo', 'Matisse', 'Utamaro'];

artists.forEach(artist => {
  console.log(artist + ' is one of my favorite artists.');
});

const numbers = [1, 2, 3, 4, 5];

const squareNumbers = numbers.map(number => {
  return number * number;
});

console.log(squareNumbers);

const things = ['desk', 'chair', 5, 'backpack', 3.14, 100];

const onlyNumbers = things.filter(thing => {
  return typeof thing === 'number';
});

console.log(onlyNumbers);

const animals = ['hippo', 'tiger', 'lion', 'seal', 'cheetah', 'monkey', 'salamander', 'elephant'];

const foundAnimal = animals.findIndex(animal => {
  return animal === 'elephant';
});

const startsWithS = animals.findIndex(index => {
  return index[0] === 's';
});

const words = ['unique', 'uncanny', 'pique', 'oxymoron', 'guise'];
console.log(words.some((word) => {
  return word.length < 6;
}));

// More iterators
const cities = ['Orlando', 'Dubai', 'Edinburgh', 'Chennai', 'Accra', 'Denver', 'Eskisehir', 'Medellin', 'Yokohama'];

const nums = [1, 50, 75, 200, 350, 525, 1000];

// Choose a method that will return undefined
cities.forEach(city => console.log('Have you visited ' + city + '?'));

// Choose a method that will return a new array
const longCities = cities.filter(city => city.length > 7);

// Choose a method that will return a single value
const word = cities.reduce((acc, currVal) => {
  return acc + currVal[0]
}, "C");

console.log(word)

// Choose a method that will return a new array
const smallerNums = nums.map(num => num - 5);

// Choose a method that will return a boolean value
nums.every(num => num < 0);

// Objects
let spaceship = {
  homePlanet: 'Earth',
  color: 'silver',
  'Fuel Type': 'Turbo Fuel',
  numCrew: 5,
  flightPath: ['Venus', 'Mars', 'Saturn']
};

let variable = spaceship.numCrew;
let variable1 = spaceship.flightPath;

// Bracket notation
let isActive = spaceship['Active Mission'];
console.log(isActive);

// Methods
let retreatMessage = 'We no longer wish to conquer your planet. It is full of dogs, which we do not care for.';

let alienShip = {
  retreat() {
    console.log(retreatMessage)
  },
  takeOff() {
    console.log('Spim... Borp... Glix... Blastoff!')
  }
};

alienShip.retreat();
alienShip.takeOff();

let spaceship2000 = {
  passengers: [{name: 'Space Dog'}],
  telescope: {
    yearBuilt: 2018,
    model: "91031-XLT",
    focalLength: 2032 
  },
  crew: {
    captain: { 
      name: 'Sandra', 
      degree: 'Computer Engineering', 
      encourageTeam() { console.log('We got this!') },
     'favorite foods': ['cookies', 'cakes', 'candy', 'spinach'] }
  },
  engine: {
    model: "Nimbus2000"
  },
  nanoelectronics: {
    computer: {
      terabytes: 100,
      monitors: "HD"
    },
    'back-up': {
      battery: "Lithium",
      terabytes: 50
    }
  }
}; 

let capFave = spaceship2000.crew.captain['favorite foods'][0];
let firstPassenger = spaceship2000.passengers[0];

// Pass by reference
let spaceship3000 = {
  'Fuel Type' : 'Turbo Fuel',
  homePlanet : 'Earth'
};

// Write your code below
let greenEnergy = objectParam => {
  objectParam['Fuel Type'] = 'avocado oil';
};

let remotelyDisable = objectParam => {
  objectParam.disabled  = true;
};

greenEnergy(spaceship3000);
remotelyDisable(spaceship3000);
console.log(spaceship3000);

// Looping through objects
let spaceship4000 = {
  crew: {
  captain: { 
      name: 'Lily', 
      degree: 'Computer Engineering', 
      cheerTeam() { console.log('You got this!') } 
      },
  'chief officer': { 
      name: 'Dan', 
      degree: 'Aerospace Engineering', 
      agree() { console.log('I agree, captain!') } 
      },
  medic: { 
      name: 'Clementine', 
      degree: 'Physics', 
      announce() { console.log(`Jets on!`) } },
  translator: {
      name: 'Shauna', 
      degree: 'Conservation Science', 
      powerFuel() { console.log('The tank is full!') } 
      }
  }
};

// for...in
for (let crewMember in spaceship.crew) {
  console.log(`${crewMember}: ${spaceship.crew[crewMember].name}`)
};
for (let crewMember in spaceship.crew) {
  console.log(`${spaceship.crew[crewMember].name}: ${spaceship.crew[crewMember].degree}`)
};

// Advanced Objects
const robot = {
  _energyLevel: 100,
  recharge(){
    this._energyLevel += 30;
    console.log(`Recharged! Energy is currently at ${this._energyLevel}%.`)
  }
};

robot._energyLevel = 'high';
robot.recharge()

// Geters and Seters
const person = {
  _firstName: 'John',
  _lastName: 'Doe',
  get fullName() {
    if (this._firstName && this._lastName){
      return `${this._firstName} ${this._lastName}`;
    } else {
      return 'Missing a first name or a last name.';
    }
  }
}
 
// To call the getter method: 
person.fullName; // 'John Doe'

const person1 = {
  _age: 37,
  set age(newAge){
    if (typeof newAge === 'number'){
      this._age = newAge;
    } else {
      console.log('You must assign a number to age');
    }
  }
};

// Factory functions
const monsterFactory = (name, age, energySource, catchPhrase) => {
  return { 
    name: name,
    age: age, 
    energySource: energySource,
    scare() {
      console.log(catchPhrase);
    } 
  }
};

const ghost = monsterFactory('Ghouly', 251, 'ectoplasm', 'BOO!');
ghost.scare(); // 'BOO!'

// Destructured assignment
const robot1 = {
  model: '1E78V2',
  energyLevel: 100,
  functionality: {
    beep() {
      console.log('Beep Boop');
    },
    fireLaser() {
      console.log('Pew Pew');
    },
  }
};

const { functionality } = robot1;
functionality.beep();