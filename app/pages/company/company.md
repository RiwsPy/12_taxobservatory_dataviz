[//]: # (Layout of company page)

[//]: # (Main content)
<main_content|part|class_name=main-page-style|

[//]: # (1. Select company section)
<selection|part|class_name=main-content|
<|layout|columns=1fr 1fr|gap=1.5rem|class_name=align-columns-top|
<|part|
Pick a company to dive into the report
{: .big_title_blue .pr4 .mb2}

<|{selected_company}|selector|lov={selector_company}|on_change=on_change_company|dropdown|class_name=fullwidth mb2|width=65%|>

<|part|class_name=align-items-bottom|
Can't find a company ?<br/>
We might have missed out in its report.<br/>
Reach with this [contact form](/Contact) if you found it.
{: .text_blue .contact_text .pt2 }
|>
|>

<|{header_right_image_path}|image|width=100%|>
|>
|selection>

<hr class="header_hr" />

[//]: # (2. Company general information section)
<company|part|class_name=main-content|
<|{selected_company}|text|class_name=big_title_blue|>

<|layout|columns=1fr 1fr 1fr 1fr|gap=1.5rem|class_name=align-items-center mt1|
<|card|
<|part|
<|{viz_1.title}|text|class_name=viz_title|>
<br/>
<|{viz_1.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|class_name=viz_text_blue|
<|{viz_1.data}|>
|>
|>

<|card|
<|part|
<|{viz_2.title}|text|class_name=viz_title|>
<br/>
<|{viz_2.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|class_name=viz_text_blue|
<|{viz_2.data}|>
|>
|>

<|card|
<|part|class_name=pb1|
<|{viz_3.title}|text|class_name=viz_title|>
<br/>
<|{viz_3.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=round mb1|
<|{viz_3.data}|>
|>
|>

<|card|
<|part|class_name=pb1|
<|{viz_4.title}|text|class_name=viz_title|>
<br/>
<|{viz_4.sub_title}|text|class_name=viz_sub_title|>
|>
<|part|class_name=round mb1|
<|{viz_4.data}|><|/100|text|>
|>
|>
|>
|company>

[//]: # (3. Financial reporting section)
<financial|part|class_name=main-content|

[//]: # (Financial section : title and selector)
<title|part|class_name=title_selector_container mb2|
Financial Reporting Overview
{: .big_title_blue }

<|{selected_year}|selector|lov={selector_year}|on_change=on_change_year|dropdown|class_name=fullwidth|>
|title>

[//]: # (3.1. Financial section : tax transparency)
<tax_transparency|part|
Tax transparency
{: .title_blue .mb2}

<|layout|columns=1fr 3fr|gap=1.5rem|
<|card|
<|part|class_name=pb1|
<|{viz_5.title}|text|class_name=viz_title|>
<br/>
<|{viz_5.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|class_name=round mb1|
<|{viz_5.data}|><|/100|text|>
|>
|>

<|card|
<|part|class_name=pb1|
<|{viz_26.title}|text|class_name=viz_title|>
<br/>
<|{viz_26.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|
<|{viz_26.data}|table|show_all|style=table-cell|class_name=rows-similar|>
|>
|>
|>

<|part|class_name=text_justified mt2|
* We evaluate the reports transparency considering two features: the geographical disaggregation and the presence of 
the different recommended variables. The more detailed the geographical disaggregation and the higher the number of 
variables published the higher the transparency score. Find more on our [methodology page](/Methodology).
<br/><br/>
* It is important to note that the availability of different variables will be essential to calculate the indicators 
below. When the variables are not available it will not be possible to calculate all indicators.
|>
|tax_transparency>

[//]: # (3.2 Financial section : financial profile)
<financial_profile|part|class_name=mt2 mb4|
Financial profile
{: .title_blue .mb2}

<|layout|columns=1fr 1fr|gap=1.5rem|
<|card|
<|part|class_name=pb1|
<|{viz_13.title}|text|class_name=viz_title|>
<br/>
<|{viz_13.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|
<|{viz_13.data}|table|show_all|dynamic=True|style=table-cell|class_name=rows-similar|>
|>
|>

<|card|
<|part|class_name=pb1|
<|{viz_14.title}|text|class_name=viz_title|>
<br/>
<|{viz_14.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|
<|chart|figure={viz_14.fig}|>
|>
|>
|>
|financial_profile>

[//]: # (3.3. Financial section : distribution of profits vs employees)
<profits_employees|part|class_name=mt2 mb4|
Distribution of profits vs employees
{: .title_blue .mb2}

<|layout|columns=1fr 1fr|gap=1.5rem|
<|card|
<|part|class_name=pb1|
<|{viz_15.title}|text|class_name=viz_title|>
<br/>
<|{viz_15.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|height=400px|class_name=scrollable-container|
<|chart|figure={viz_15.fig}|>
|>
|>

<|card|
<|part|class_name=pb1|
<|{viz_16.title}|text|class_name=viz_title|>
<br/>
<|{viz_16.sub_title}|text|class_name=viz_sub_title|>
<br/>
|>
<|part|
<|chart|figure={viz_16.fig}|>
|>
|>
|>

<|part|class_name=text_justified mt2|
This chart plots the percentage of total positive profits and the percentage of total employees reported in each 
country where the multinational is active. Comparing the amount of physical production factors like employees with 
the amount of profit can give an indication of profit shifting activities where strong misalignment are observed
|>

|profits_employees>
|financial>
|main_cont>