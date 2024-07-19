# Core Orion Data Types, Structures, Report Standardization
#### We're  Always Discretionary With Stochasity.

We are a Cyber, Product, Research and Process Automation Organization. Accurate data is our life blood. We aspire to deploy the right tools for the right job, at the right time arcing toward high enough accuracy to be relied on.

The Why? The nature of Language Models both Large and Small is probabilistic. Unlike in traditional software engineering there is no guarantee that data returned will be consistent, nor as the user expected when it comes to formatting. In order to minimize false positives and false negatives the Orion project will implement strict data structure and document control, as well as third party tools. Cyber is an industry with serious consequences and we will be progressively testing and deploying our solutions with care.

It is the nature of a new industry or discipline to be experimental and therefore all participants should keep an experimental
mindset and the Product team informed on what the SOA tools are in each domain and engage in continuous testing.

Ultimately, when the team has standardized the project's data flow and results we will train our own models specifically
for each operation from `data collection`, the `converting data to intelligence` to the multiple `agent workflows` that will continue to improve as Research does.


### Standardized Data
- Events
- Triage Reports
- Alert Reports
- Intelligence Reports
- Intelligence Briefs

### Standardization
- JSON
  - Elastic Common Scheme for cosumption by Elastic/OpenSearch
- Prompting must always include data format
- GPT4 as Judge
- Small Language Model as Judge once sufficiently fine tuned
- Human in the Loop for any series of rejected reports or alerts (n=[0,10])
- All reports should have the ability to refer to the state of the previous report in the chain.
- Develop metrics for the performance of the system as a whole
- Periodic sampling program.


### To DO:
- State Management planning.
- Consider how confidence level could be variable and judged.
- Implement Human in the Loop functionality as a P1
- Choose between Guardrails and BenchLLM or other standardization tool
- Develop types and routinely update them but in batches and version controlled
- Try cyber-phi-small against it once fine tuned
- Implement caching