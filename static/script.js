

function showOptions() {
    const problemType = document.getElementById("problem_type").value;

    const hardware = document.getElementById("hardware_valg");
    const software = document.getElementById("software_valg");
    const network = document.getElementById("network_valg");

    // Hide all first
    hardware.style.display = "none";
    software.style.display = "none";
    network.style.display = "none";

    // Show selected
    if (problemType === "hardware") {
        hardware.style.display = "block";
    }
    else if (problemType === "software") {
        software.style.display = "block";
    }
    else if (problemType === "network") {
        network.style.display = "block";
    }
}

//function nvan() { }

//  if (condition1) {   }
//   else if (condition2) {  } 
//   else { }

//  if (condition1 === '22' && condition2 === '11')   utfører hvis condition1 og condition2 er riktige

    //input
    //const navn = document.getElementById("navn").value;
    //console.log(navn);

    //output
    //document.getElementById("output").innerHTML = "Hello World";

    // leger til text i teden for å erstatte
    //document.getElementById("output").innerHTML += "Hello World";

//const nvan = navn2;   can ikke redigeres 
//let nvan = navn2;     kan redigeres

// for(var i = 0; i <= 12; i++) { } // looper fra 0 til 12
// while (true) { } looper til den blir stoppet


//window.location.href = "link"; // Change this URL to your first target

//  random number 
    //  Returns a random integer from 0 to 9:
    //  Math.floor(Math.random() * 10);

    //returns a random number between min and max (both included):
    // return Math.floor(Math.random() * (max - min + 1) ) + min;
//array
    //make an array                         let arr = [1, 2, 3, 4, 5]; // Array Declaration
    //Print the entire array                console.log(arr);
    //reverse array                         arr.reverse();
    //sort array                            (a, b) => a - b); // Ascending               arr.sort((a, b) => b - a); // Descending
    //Merge Two Arrays                      let merged = [...arr1, ...arr2];
    //remove duplicates let arraynavn       [...new Set(arr)];          arr.filter((item, index) => arr.indexOf(item) === index);
    //Find Maximum and Minimum              let max = Math.max(...arr);     let min = Math.min(...arr);
    //Sum of All Elements                   let sum = arr.reduce((acc, val) => acc + val, 0);
    //Check if Array Includes a Value       arr.includes(5);  // true or false
    //Find First Matching Element           let found = arr.find(x => x > 10);
    //Remove Specific Element               arr = arr.filter(item => item !== valueToRemove);
    //Get Unique Elements Only              let unique = arr.filter((item, index) => arr.indexOf(item) === index);

    
//sumboler    
    //   +  Addition
    //   -	Subtraction
    //   *	Multiplication
    //   **	Exponentiation 2^2
    //   /	Division
    //   %	Modulus (Division Remainder)
    //   ++	Increment
    //   --	Decrement

    // ==	equal to
    // ===	equal value and equal type
    // !=	not equal
    // !==	not equal value or not equal type
    // >	greater than
    // <	less than
    // >=	greater than or equal to
    // <=	less than or equal to
    // ?	ternary operator

    // &	&&  AND	
    // |    ||	OR	
    // ~	    NOT	
    // ^	    XOR