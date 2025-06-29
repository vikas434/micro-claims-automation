# Micro-Claims Automation with Google's Multi-Agent Toolbox

This repository contains the code for automating micro-claims processing using Google's Multi-Agent Toolbox (ADK). This solution transforms the traditionally frustrating experience of warranty claims into a swift, 60-second settlement, leveraging the power of AI agents.

## Overview

Inspired by the success of AI agents in automating grocery shopping, this project tackles the challenge of micro-claims in the insurance and retail warranty sectors. By automating tasks like policy verification, damage assessment, and fraud screening, we can significantly reduce operational costs and enhance customer satisfaction.

## The 60-Second Settlement Pipeline

Our solution is built around a streamlined, sequential pipeline of four specialized AI agents:

- **Policy-Check:** Verifies warranty eligibility.
- **Vision-Damage:** Assesses damage using Gemini Vision.
- **Fraud-Screen:** Detects fraudulent claims.
- **Payout:** Issues instant credits or e-gift cards.

This entire workflow is orchestrated by Google's Agent Development Kit (ADK), defined in a concise YAML file.

## Project Structure

```
├── micro_claims.yaml
└── agents
    ├── policy_check.py
    ├── vision_damage.py
    ├── fraud_screen.py
    └── payout.py
```

- `micro_claims.yaml`: Defines the overall workflow and agent orchestration.
- `agents/`: Contains the Python scripts for each individual AI agent.

## Getting Started

To get this project up and running, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/micro_claims_automation.git
    cd micro_claims_automation
    ```
2.  **Set up environment variables:**
    You will need to set the following environment variables:
    - `DB_DSN`: Database connection string for the policy check agent.
    - `GCP_PROJECT`: Your Google Cloud Project ID for Gemini Vision.
    - `WEAVIATE_URL`: URL for your Weaviate instance (for fraud screening).
    
    Example:
    ```bash
    export DB_DSN="your_db_dsn"
    export GCP_PROJECT="your_gcp_project_id"
    export WEAVIATE_URL="your_weaviate_url"
    ```
3.  **Deploy with ADK:**
    ```bash
    adk deploy micro_claims.yaml
    ```

## Screenshots (Refer to the Medium Blog Post for Visuals)

For a visual representation of the process and key components, please refer to the original Medium blog post:

- **The 60-Second Settlement Illustration:** This image visually captures the essence of speed and automation in our claims process.
- **Cracked Phone Screen Example:** An image illustrating the common scenario this solution addresses.
- **Architecture Diagram:** A Mermaid diagram showcasing the flow and interaction of the AI agents within the pipeline.

[Link to the Medium Blog Post](https://medium.com/google-cloud/effortless-grocery-shopping-creating-an-ai-agent-with-gemini-to-automate-your-purchases-a1c51973633b)

## License

This project is licensed under the MIT License - see the LICENSE file for details.



