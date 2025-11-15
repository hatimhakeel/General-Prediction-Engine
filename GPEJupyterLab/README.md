# GPE Jupyter Lab

## Configure Python virtual environment

1. Open CLI application (e.g. Windows PowerShell ISE)
2. Go to GPEJupyterLab folder
3. Create Python virtual environment
   ```
   python -m venv gpejlvenv
   ```
4. Go to the virtual environment Scripts\
5. Activate
   ```
   .\Activate.ps1
   ```

## Install and run JupyterLab

1. From activated CLI session, install the JupyterLab coding notebook project
   ```
   pip install jupyterlab
   ```
2. Run JupyterLab
   ```
   jupyter lab
   ```

## ML data exploration & visualization

1. Go to Jupyter Lab web url
2. Create a new workspace name "labnotebooks"
3. Go to the workspace
4. Create the ML workbook
5. Save with model, graphs & results

## Test API endpoints

1. Start the GEP server
2. Generate AI model
   ```Power Shell
   Invoke-WebRequest -Uri "http://localhost:{port}/sales_forecast/train/{merchant-id}" | Select-Object -ExpandProperty Content
   Invoke-WebRequest -Uri "http://localhost:8888/sales_forecast/train/1" | Select-Object -ExpandProperty Content
   ```
3. Forecast sales
   ```Power Shell
   Invoke-WebRequest -Uri "http://localhost:{port}/sales_forecast/{merchant-id}/{forecast-period}" | Select-Object -ExpandProperty Content\
   Invoke-WebRequest -Uri "http://localhost:8888/sales_forecast/1/31" | Select-Object -ExpandProperty Content
   ```
