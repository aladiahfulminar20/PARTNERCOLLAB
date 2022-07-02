// INTRO TO JAVASCRIPT -----------------------------------------

//console.log("I like Jalie!");
//console.log("I like pizza!");

//window.alert("I REALLY LIKE JALIE!");

// THIS IS A COMMENT

/*

 THIS IS A MULTILINE COMMENT
 ZZZ

*/

// JAVASCRIPT VARIABLES -----------------------------------------

//let firstName = "Aladiah";  // STR VAR
//let lastName = "Fulminar";

//let age = 19; // INT VAR

//BOLEAN VAR
//let student = true;

//age = age + 1;

/*
console.log("Hello,", firstName, lastName);
console.log("Perhaps your age is ", age)
console.log("And according to the database you're a student which is in boolean it is", student);

document.getElementById("p1").innerHTML = "Hello, " + firstName +  " "  + lastName;
document.getElementById("p2").innerHTML = "And you are " + age + " years old.";
document.getElementById("p3").innerHTML = "Enrolled: " + student;
*/

// ARITHMETIC EXPRESSIONS -----------------------------------------

/*

    arithmetic expression is a combination of operands (values, variables, etc.)
    operators (+ - * / %)
    that can be evaluated to a value
    ex. y = x + 5;

    operator precendence

    1. parenthesis ()
    2. exponents
    3. multiplication & division
    4. addition & subtraction

*/

/*
let students = 20;

// students = students + 1;

// Augmented Assignment Operator Example:

students *= 2; // equivalent of students = students (operator) 1;

console.log(students);
*/

// JAVASCRIPT INPUT -----------------------------------------

/*
let username = window.prompt("What's your name?");

console.log(username);
*/

/*
document.getElementById("myButton").onclick = function(){

    username = document.getElementById("myText").value;
    console.log(username);
    document.getElementById("myLabel").innerHTML = username;
}
*/

// TYPE CONVERSION -----------------------------------------

/*
let age = window.prompt("How old are you?");

console.log(typeof age);
age = Number(age);
console.log(typeof age);
age += 1;


console.log("Happy Birthday! You are", age, "years old");
*/

/*
let x, y, z;

x = Number("3.14");
y = String(3.14);
z = Boolean("pizza");

console.log(x, typeof x);
console.log(y, typeof y);
console.log(z, typeof z);
*/

// VARIABLE CONSTANTS -----------------------------------------

/*
const PI = 3.14159;
let radius;
let circumference;

radius = window.prompt("Enter the radius of a circle");
radius = Number(radius);

circumference = 2 * PI * radius;

console.log("The circumference is:", circumference);
*/


// MATH -----------------------------------------

/*
let x = 3.14;
let y = 5;
let z = 9;

let maximum;
let minimum;

//x = Math.floor(x);
//x = Math.floor(x);
//x = Math.ceil(x);
//x = Math.pow(x, 2);
//x = Math.sqrt(x);
//x = Math.abs(x);

//maximum = Math.max(x, y, z);
//minimum = Math.min(x, y, z);

x = Math.PI;
console.log(x);
*/

