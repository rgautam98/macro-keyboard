# Macro Keyboard 


## Inspiration 
This project is inspired from the cockpit of an Airbus A350. Basically, I asked myself a question. Why do you need so many buttons and screens?  
Rather, why dont you provide the pilots with a terminal and have them execute the commands there. 

After asking the same to a couple of pilots(both line training and flying), the most common answer I could get(apart from the technical ones) is ease of use and productivity. I then wanted to apply the same to my daily software engineering lifecycle.  

I started to look into lua macros and its usage in linux. The setup was complicated and I could not get it working in the way I wanted. So, I started this python project. It was easier to setup and integrates well into my existing python codebase, for other actions.   

## Codebase 

This is a no nonsense quick and dirty implementation of a macro keyboard software to simplify certain workflows in my day to day life.  

I basically bought a basic keyboard, plugged it in, put together pieces of code I could find on the internet and brought this to where it is. 

The main keymaps can be found in the file KeyboardConfig.py 


Just clone this repo, install the dependencies, add whatever functions you want to in the keyboard config, plugin an external keyboard, and voila, you have a macro keyboard.  

At the moment, I have put in a couple of macros for vscode, terminal and an api call as an example. This is just to show you a couple of examples on how the sdk can be used. 

Any ideas on improvement/customization and any interesting macros you can think of that can help others, are also welcome. Just open an issue in GitHub or open a pull request. 