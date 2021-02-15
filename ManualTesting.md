# Some of the manual tests that I would perform outside the automation scripts are mentioned below:

    1. GUI Test Cases
        I. Check if the the cursor is on the first name textbox when the user lands on the create account page.
        II. Check for the spelling errors in the create account page.
        III. Check that the Create Account button is diabled until all input fields are filled.
        Iv. Check if the Sign In button is enabled at all times.
        
    2. Positive Test Cases
        I. Check if the create Account button is enabled once the user enters all fields.
        II. Check if once the user fills all the fields according to Valid Input Table, the user's new account page is displayed.
        III. If the user clicks on the Sign In button, the user should be directed to the Sign In page.
         
    3. Negative Test Cases
        II. If the first name entered by user contains number and all other fields are valid, display the error message " Username cannot contain number".
        III. Check if the last name entered by user contains number and all other fields are valid, display the error message " Last name cannot contain number."
        IV. Check if the email doesn't contain '@domain_name' and all other fileds are valid, display the error message " Email is not valid"
        V. Check if the checkbox for terms and agreement is not selected and all other fields are valid, display the error message "You must agree to Terms of use".
        VI. Check if the captcha is solved and all other fields are valid, display the error message " Recaptcha is required ".
        VIII. Check if the email is already used by an user to create an account and all other fields are valid,  display the error message " Email already exists".
        IX. If two or more fields entered by user is invalid and the user clicks Create Account, displays all the corresponding error messages.