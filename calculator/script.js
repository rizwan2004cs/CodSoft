let string = "";
let memory = 0; // For memory functionalities
let input = document.querySelector("input");
let resultDisplayed = false; // Track if result was displayed
let lastOperator = ""; // Variable to store the last entered operator

const buttons = document.querySelectorAll(".button");

Array.from(buttons).forEach((button) => {
  button.addEventListener("click", (e) => {
    const value = e.target.innerText.trim();

    if (value === "=") {
      try {
        // Evaluate the expression safely
        string = eval(string);
        if (string === Infinity || string === -Infinity || isNaN(string)) {
          throw new Error("Invalid calculation");
        }
        resultDisplayed = true; // Mark that result is displayed
        lastOperator = ""; // Reset last operator after evaluating
      } catch (error) {
        string = "Error";
        resultDisplayed = true; // Mark that result is displayed
        lastOperator = ""; // Reset last operator on error
      }
    } else if (value === "C") {
      string = "";
      resultDisplayed = false;
      lastOperator = ""; // Clear last operator
    } else if (value === "%") {
      try {
        string = (eval(string) / 100).toString();
        resultDisplayed = true; // Mark that result is displayed
        lastOperator = ""; // Reset last operator after calculating percentage
      } catch {
        string = "Error";
        resultDisplayed = true; // Mark that result is displayed
        lastOperator = ""; // Reset last operator on error
      }
    } else if (value === "AC") {
      string = "";
      resultDisplayed = false;
      lastOperator = ""; // Clear last operator
    } else if (value === "M") {
      string = memory.toString();
      resultDisplayed = false;
      lastOperator = ""; // Clear last operator
    } else {
      if (resultDisplayed) {
        if (['+', '-', '*', '/'].includes(value)) {
          // If result is displayed and a new operator is pressed
          if (lastOperator) {
            // Evaluate current expression before adding the new operator
            try {
              string = eval(string);
              if (string === Infinity || string === -Infinity || isNaN(string)) {
                throw new Error("Invalid calculation");
              }
            } catch (error) {
              string = "Error";
              resultDisplayed = true; // Mark that result is displayed
              lastOperator = ""; // Reset last operator on error
              return;
            }
          }
          string += value;
          lastOperator = value; // Update last operator
          resultDisplayed = false;
        } else {
          // Start new expression with the new number
          string = value;
          resultDisplayed = false;
        }
      } else {
        if (['+', '-', '*', '/'].includes(value)) {
          // If an operator is pressed
          if (/[+\-*/]$/.test(string)) {
            // If the string already ends with an operator, replace it
            string = string.replace(/[\+\-\*\/]$/, value);
          } else {
            // Add new operator if none exists at the end
            string += value;
          }
          lastOperator = value; // Store the current operator
        } else {
          // Append the number to the string
          string += value;
        }
      }
    }

    // Update input value
    input.value = string;
  });
});
