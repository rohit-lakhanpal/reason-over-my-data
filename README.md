# Add details ...

## Setup

1. Clone the repository
    ```
    git clone https://...
    ```
1. Create cloud resources
    1. An instance of the Azure OpenAI service with the following models deployed:
        - gpt-4
        - text-embedding-ada-002
    1. An instance of the Azure AI Search service
    1. An instance of an Azure Storage account
1. Create environment variables by copying the `.env.sample` file to `.env` and filling in the values
    ```
    cp .env.sample .env
    ```
    