# Instruction on running the program on windows using Pycharm
    1. Install Python, browsers, browser drivers, Pycharm
        Open the project in Pycharm
        
    2. Create a virtual enviroment. 
        To do so, Go To Settings, 
        Click on Project Structure.
        Click setting symbol and add a virtual env
    
    3. Install the requirements. Click on Terminal and run:
        ` pip3 install -r requirements.txt `
        
    4. Configure the driver path.
        To do so, Open the conftest.py file.
        Put the path of your driver in the driver instantiation in setup method
    
    5. Run the following command:
        ` pytest -v -s test_createAccount.py --browser your_browser `
        For instance, If you are using Chrome,
        ` pytest -v -s test_createAccount.py --browser chrome `
        
# Instruction on running the program on linux/Unix/ubuntu

    1. Install Python, browsers, browser drivers.
        cd tesla_challenge
        
    2. Create a virtual environment.
        ` sudo python3 -m venv env `
        
    3. Activate the virtual environment.
        ` source env/bin/activate `
        
        Give access to the parent directory 
    4. Install the requirements.
        ` sudo pip3 install -r requirements.txt`
        
    5. Configure the driver path.
        To do so, Open the conftest.py file.
        Put the path of your driver in the driver instantiation in setup method
    
    6. Give Sudo privileges to the working dir.
        ` sudo chown -R username  /home/username/tesla_challenge`
        
    7. Run the following command:
        ` pytest -v -s test_createAccount.py --browser your_browser `
        For instance, If you are using Chrome,
        ` pytest -v -s test_createAccount.py --browser chrome `