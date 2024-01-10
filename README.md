# PGPortfolio-MarketCollector

## Market Chart Collector for DRL Portfolio Management System

This project focuses on collecting market charts from the Poloniex website, performing preprocessing on the acquired data, and creating a base dataset for a Deep Reinforcement Learning (DRL) project. The dataset generated through this process serves as a foundation for training and evaluating DRL models in the cryptocurrency portfolio management system.

### Project Structure

The project is organized into three main folders:

1. **MarketCollector:**
   - **Purpose:** Obtain historical market data in SQLite format from the Poloniex Previous API.
   - **Source:** This folder is derived from the work originally found in [Iffix's GitHub repository](https://github.com/iffiX/PGPortfolio-pytorch) and has been slightly modified to accommodate the newer version of the Poloniex API.

2. **Preprocessing:**
   - **Purpose:** Conduct preprocessing on the dataset, converting SQLite files into CSV format, and separating individual coin data into distinct CSV files.

3. **New API:**
   - **Purpose:** Contains a Jupyter file for Implements a new market collector using the updated API, ensuring compatibility with the latest changes and obtaining market charts for high-volume cryptocurrencies.

### Getting Started

To use this project, follow these steps:

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/FarshidSadeghian/PGPortfolio-MarketCollector.git
   ```

2. Navigate to each folder (`MarketCollector`, `Preprocessing`, `New API`) and follow the specific instructions provided in their respective README files.

### Dependencies

Ensure that you have the required dependencies installed before running the project. You can find the necessary packages listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Acknowledgments

- Special thanks to [Iffix](https://github.com/iffiX) for the initial inspiration and codebase.

Feel free to reach out for any questions, issues, or improvements. Happy coding!