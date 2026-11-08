# Power BI rebuild notes

The source article describes a Power BI workflow using an Excel dataset, Power Query transformations, month sequencing, and DAX measures.

## Suggested measures

```DAX
Revenue = SUM(Sales[Revenue])
Profit = SUM(Sales[Profit])
Units Sold = SUM(Sales[Units Sold])
Average Selling Price = DIVIDE([Revenue], [Units Sold])
Profit Margin = DIVIDE([Profit], [Revenue])
```

## Suggested report pages

1. **Executive overview:** revenue, profit, units sold, average selling price, and profit margin.
2. **Category performance:** revenue and units sold by category, with a revenue-versus-demand comparison.
3. **Geography and time:** monthly and regional analysis using a correctly ordered month field.
4. **Brand and customer trends:** brand comparison and filters for customer satisfaction metrics where available.

The article does not publish the original Excel workbook or the complete row-level data, so this repository intentionally does not fabricate those missing fields.
