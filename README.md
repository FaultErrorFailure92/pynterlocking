# Pynterlocking  
A Non-Safe Interlocking Kernel in Python3  

## Why?  
Pynterlocking is my latest "kitchen-sink" project, where I aim to develop a functioning (albeit non-safe) interlocking kernel in Python 3. The goal is to model all essential infrastructure elements and implement a route-setting logic. Once that is complete, I plan to add a user interface (UI) to bring everything together.  

## Architecture
``` to be done in the future


## Testing
``` to be done in the future

## Features  

### Infrastructure Elements  
You can currently create and manage the following infrastructure elements, each with unique but basic properties:  

- **Generic Elements**  
- **Tracks**  
- **Points**  
- **Signals**:  
  - Generic Light Signals  
  - Main Signals  
  - Shunting Signals  
  - Distant Signals  
  - Protection Signals  
  - Signal Repeaters  
- **Level Crossings**  
- **Routes**  

### Route Setting  
Route setting logic is under development and includes:  

- Determining if the route is for a train or shunting movement  
- Searching for distinct standard routes or alternative detour routes  

### Planned Features  
Future enhancements will focus on improving the kernel's functionality and extensibility:  

- Importing topology data from JSON files  
- Implementing flank protection to ensure safe switching and routing  
- Adding route protection mechanisms  

## Roadmap  
1. Finalize the core route-setting logic  
2. Implement JSON topology importer  
3. Introduce safety features like flank and route protection  
4. Develop a user-friendly UI

## Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/pynterlocking.git
   python ./main.py

## Usage example
``` to be done in the future

## Known Issues
As it is under development anyway, this part will be done in the future. 

## Contributing  
Contributions are welcome! Whether it's suggestions, bug fixes, or feature implementations, feel free to open an issue or submit a pull request.

## License  
Not licensed yet.

---

Stay tuned as this project evolves! 🚂  
