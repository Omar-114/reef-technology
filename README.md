## 1. Install Flask

Install Flask using pip:
```bash
pip install Flask
```

## 2. Create virtual environment

```bash
python -m venv venv
```

## 3. Activate virtual environment

- Windows
```bash
venv\Scripts\activate
```

- macOS
```bash
source venv/bin/activate
```

## 4. Install python libraries with pip
```bash
pip install -r requirements.txt
```

## 5. Install wkhtmltopdf
- Windows:
  - Download the installer from the [wkhtmltopdf downloads page](https://wkhtmltopdf.org/downloads.html).
  - Run the installer and follow the instructions.
- macOS:
  - You can install wkhtmltopdf using Homebrew:
    ```Bash
    brew install wkhtmltopdf
    ```

- Linux:
  - On Debian/Ubuntu-based systems, you can install it using:
    ```Bash
    sudo apt-get install wkhtmltopdf
    ```
  - For Red Hat-based systems, you can use:
    ```bash 
    sudo yum install wkhtmltopdf
    ```

## 6. Setup daily cronjob
-  Open the crontab configuration for editing:
```bash
crontab -e
```

- Add a new line to schedule the job. To run the script every day at 0 AM(Midnight), add the following line:
```bash
0 0 * * * /usr/bin/python3 /utils/cron_wrapper.py
```
The cron job will generate a pdf file daily. The generated file name should be look like this: [employee_timesheet_2024-09-12.pdf]
- Check Cron job logs
You can check the cron job logs to ensure it runs correctly. Logs are typically found in /var/log/syslog or /var/log/cron.log, depending on your system configuration.

## 7. [Optional] Run the application
```bash
python app.py
```

## 8, Run test cases

```bash
python -m unittest api/test_reef_api.py
```