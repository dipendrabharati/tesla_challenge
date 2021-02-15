# Instruction on running the program on windows using Pycharm
    1. Create a virtual enviroment. 
        To do so, Go To Settings, 
        Click on Project Structure.
        Click setting symbol and add a virtual env
    
    2. Install the requirements. Click on Terminal and run:
        ` pip3 install -r requirements.txt `
        
    3. Configure the driver path.
        To do so, Open the conftest.py file.
        Put the path of your driver in the driver instantiation in setup method
    
    3. Run the following command:
        ` pytest -v -s test_createAccount.py --browser your_browser `
        For instance, If you are using Chrome,
        ` pytest -v -s test_createAccount.py --browser chrome `
        
# Instruction on running the program on linux/Unix/ubuntu

    1. Install Python.
        ` sudo apt-get install python3.8 `
        
    2. Create a virtual environment.
        ` sudo python -m venv env `
        
    3. Activate the virtual environment.
        ` source env/bin/activate `
        
    4. Install the requirements.
        ` pip3 install -r requirements.txt`
        
    5. Configure the driver path.
        To do so, Open the conftest.py file.
        Put the path of your driver in the driver instantiation in setup method
    
    3. Run the following command:
        ` pytest -v -s test_createAccount.py --browser your_browser `
        For instance, If you are using Chrome,
        ` pytest -v -s test_createAccount.py --browser chrome `