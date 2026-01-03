## Inventory Management for Retail — Stochastic Demand 📈
*Implement inventory management rules based on a periodic review policy to reduce the number of store replenishments*

<p align="center">
  <a href="https://www.samirsaci.com/inventory-management-for-retail-stochastic-demand-2/" target="_blank" rel="noopener noreferrer">
    <img
      align="center"
      src="https://miro.medium.com/max/1280/1*IKoODTaPlZ1I6GdZ4vGwow.png"
      style="max-width: 100%; height: auto;"
    >
  </a>
</p>

For most retailers, inventory management systems take a fixed, rule-based approach to forecasting and managing replenishment orders.

The objective is to develop a replenishment policy that minimises ordering, holding, and shortage costs.

In a previous article, we built a simulation model based on a continuous-review inventory policy, assuming a normal demand distribution.

However, this policy can be inefficient when managing a portfolio of items with varying replenishment cycles.

### Article
In this [Article](https://www.samirsaci.com/inventory-management-for-retail-stochastic-demand-2/),  we will improve this model and implement a periodic review policy with Python to limit the number of replenishments.

### Problem Statement
As an Inventory Manager at a mid-sized retail chain, you are responsible for setting replenishment quantities in the ERP.
Because your warehouse operations manager is complaining about order frequency, you begin to challenge the replenishment rules implemented in the ERP, especially for the fast-runners.
Previously, we have implemented several inventory rules based on continuous review policies.

### Question
What would be the number of replenishments if you have 2,500 SKUs?

### Data set
This analysis will be based on Dummy Data shared in this folder.

**Note:** Please unpack the `.rar` file in the `data` folder to extract the CSV file before running the script.

## Code
In this repository, you will find all the code used to explain the concepts presented in the article.

### Files
- `Inventory Management - Stochastic Periodic.ipynb` - Jupyter notebook with step-by-step analysis
- `inventory_periodic.py` - Standalone Python script

### Getting Started
```bash
pip install -r requirements.txt
python inventory_periodic.py
```

### Dependencies
- pandas
- matplotlib
- numpy
- scipy


## About me 🤓
Senior Supply Chain and Data Science consultant with international experience working on Logistics and Transportation operations.\
For **consulting or advising** on analytics and sustainable supply chain transformation, feel free to contact me via [Logigreen Consulting](https://www.logi-green.com/).\
For more case studies, check my [Personal Website](https://samirsaci.com).
