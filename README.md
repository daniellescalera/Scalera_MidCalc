"# Scalera_MidCalc Calculator Project"
### Danielle Scalera 

## Design Patterns Used

This project implements several software design patterns to improve maintainability and structure.

### 1️ Singleton Pattern - **Ensuring a single instance for history management**
- **Description:** The Singleton pattern ensures only one instance of `CalculationHistory` exists throughout the application.
- **Implementation:** See [`calculator/history.py`](calculator/history.py), `CalculationHistory` class.

### 2️ Factory Pattern - **Plugin-based operation system**
- **Description:** The Factory pattern allows dynamic loading of calculator operations using a plugin system.
- **Implementation:** See [`calculator/plugin_factory.py`](calculator/plugin_factory.py), `PluginFactory` class.

### 3️ Strategy Pattern - **Using different calculation strategies**
- **Description:** The Strategy pattern allows switching between different arithmetic operations (`AdditionStrategy`, `SubtractionStrategy`, etc.).
- **Implementation:** See [`calculator/operations.py`](calculator/operations.py), classes for each strategy.

### 4️ Facade Pattern - **Simplifying access to calculation history**
- **Description:** The Facade pattern provides a simple interface (`HistoryFacade`) to interact with `CalculationHistory`.
- **Implementation:** See [`calculator/facade.py`](calculator/facade.py), `HistoryFacade` class.

unlisted youtube video: https://youtu.be/FN500CNc_Go