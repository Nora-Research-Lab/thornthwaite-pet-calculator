![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Thornthwaite PET Calculator
 
*For climatologists and hydrologists: enter monthly mean temperatures and latitude to instantly compute potential evapotranspiration using the Thornthwaite method.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Climate & Earth Systems
 
Functional spec: (a) Inputs: 12 monthly mean temperature values (each in °C, 0 to 50 range; number inputs with step 0.1); Latitude in decimal degrees (slider -90 to 90, step 0.5); user selects Northern or Southern Hemisphere via radio button. (b) Core calculation: Compute monthly heat index (i) for each month: i = (T/5)^1.514 if T > 0, else 0. Sum annual heat index I = sum(i). Compute alpha: a = 6.75e-7 * I^3 - 7.71e-5 * I^2 + 1.792e-2 * I + 0.49239. For each month, compute unadjusted PET (mm/month): PET_unadj = 16 * (10T/I)^a (only if T > 0, else 0). Apply daylight-hour correction factor based on latitude and month (standard Thornthwaite table lookup; store as embedded list of 12 values for each latitude band, or use the empirical formula with day length calculated from latitude and day-of-year (15th of each month). Day length (N) = (24/π) * arccos(-tan(φ)*tan(δ)) where δ is solar declination on the 15th. Compute adjustment factor = (N/12) * (days_in_month/30). Multiply PET_unadj by adjustment factor to get corrected monthly PET. Annual PET = sum of corrected monthly PET. (c) Gradio UI: Two sections side-by-side or vertical: left side input panel with 12 number inputs labeled 'Month 1 (Jan) ... Month 12 (Dec)' in °C, latitude slider, hemisphere radio. Right side shows output: a table with Month, Temperature, PET (mm/month); a bar chart of monthly PET using matplotlib; and a large numeric display of 'Annual PET (mm)'. (d) Output: table (12 rows), bar chart PNG, and annual total. No AI component, purely deterministic calculation using standard climatological method.
 
## Run it
 
```bash
docker build -t thornthwaite-pet-calculator .
docker run -p 7860:7860 thornthwaite-pet-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-10-01.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
