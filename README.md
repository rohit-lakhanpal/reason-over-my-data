<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">
    Reason over my data
  </h3>

  <p align="center">
    powered by
    <br />
    <a href="https://github.com/rohit-lakhanpal/reason-over-my-data">
        <img src="docs/img/logo.png" alt="Logo" height="80">
    </a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>    
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#disclaimer">Disclaimer</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

Reason Over My Data" is a project that helps you efficiently manage and analyze web-based data using Azure OpenAI, Azure Search, LLama Index, and Prompt Flow. It indexes your website to ensure fast and organized data retrieval and supports advanced vector searches for more precise data discovery.

After indexing, the project lets you ask questions about the data, providing insights and answers to your queries. It offers advanced tools for analyzing your approach to reason over your data by building evaluation flows. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get started with "Reason Over My Data," follow these steps:

1. **Clone the Repository:**
   First, clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/rohit-lakhanpal/reason-over-my-data
   ```

2. **Create Cloud Resources:**
   Ensure you have the necessary cloud resources ready before running the project:
   - **Azure OpenAI Service:** Deploy an instance of the Azure OpenAI service with the following models:
     - A chat model (ideally GPT-4) – [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/chatgpt)
     - text-embedding-ada-002
     - Vision models (ensure you have access and have deployed these capabilities) – [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/gpt-with-vision)
   - **Azure AI Search Service:** Set up an instance of Azure AI Search service.
   - **Azure Storage Account:** Create an Azure Storage account to manage and store data efficiently.

3. **Create Environment Variables:**
   To configure the application, copy the `.env.sample` file to `.env` and update the values:
   ```bash
   cp .env.sample .env
   ```
   Fill in the required values in the `.env` file, such as your Azure service credentials and connection details.

With these steps completed, you'll be all set to start using "Reason Over My Data."

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Technologies Explored

These usecases leverage the following technologies:
- Azure AI Vision [(learn more)](https://azure.microsoft.com/en-au/products/cognitive-services/vision-services/)
- Azure AI Content Safety [(learn more)](https://azure.microsoft.com/en-au/products/cognitive-services/content-safety/)
- Azure OpenAI [(learn more)](https://azure.microsoft.com/en-au/products/cognitive-services/openai-service/)
- Azure Machine Learning [(learn more)](https://azure.microsoft.com/en-au/products/machine-learning/)
- Azure AI Search [(learn more)](https://azure.microsoft.com/en-au/products/search/)


Major cloud technologies/frameworks/libraries are listed here:
* [![Azure][azure.com]][azure-url]
* [![OpenAI][openai.com]][openai-url]
* [![Python][python.org]][Python-url]
* [![Semantic Kernel][learn-sk]][sk-url]
* [![Llama Index][llama-index-url]][llama-index-site]
    

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. **Fork the Project**: Fork the repo you want to contribute to by clicking the Fork button on the top right corner of the repo page.
1. **Clone the Repo**: Clone the forked repo to your local machine using the command (`git clone URL_OF_FORK`).
2. **Branch**: Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. **Commit**: Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the Branch**: (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**: Go to your forked repo on GitHub and click Contribute and then Open a pull request. Fill out the details of your pull request and submit it.

Learn more about contributing to projects [here](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DISCPLAIMER -->
## Disclaimer

This template is provided "as is" without warranty of any kind, whether express or implied. Use at your own risk! The author will not be liable for any losses or damages associated with the use of this template. 

It is intended to be used as a starting point for your own project and not as a final product.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

- [Rohit Lakhanpal](https://blog.try-it.dev/author/rohit/) | [@github](https://github.com/rohit-lakhanpal) | rohit@try-it.dev
- Project Link: [https://github.com/rohit-lakhanpal/reason-over-my-data](https://github.com/rohit-lakhanpal/reason-over-my-data)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

These toolkits are never the result of solitary efforts. I wish to extend my heartfelt thanks to my friends, colleagues, and fellow community members for their exceptional contributions. We have built upon your work, and it is your efforts that have laid the foundation for our success. Your work is not only recognised but deeply valued.

* [The Prompt Flow Team]()
* [The Llama Index Team]()
* [This amazing ReadME template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- REFERENCES -->
## References
* [Using AI Search with Llama Index]https://docs.llamaindex.ai/en/stable/examples/vector_stores/AzureAISearchIndexDemo/)
* [Improving RAG performance with Azure AI Search and Azure AI prompt flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/improving-rag-performance-with-azure-ai-search-and-azure-ai/ba-p/4117118)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

> <br/> Documentation generated by AI, edited by humans. ❤️ <br/> <br/>


<p align="right">(<a href="#readme-top">back to top</a>)</p>


[contributors-shield]: https://img.shields.io/github/contributors/rohit-lakhanpal/reason-over-my-data.svg?style=for-the-badge
[contributors-url]: https://github.com/rohit-lakhanpal/reason-over-my-data/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rohit-lakhanpal/reason-over-my-data.svg?style=for-the-badge
[forks-url]: https://github.com/rohit-lakhanpal/reason-over-my-data/network/members
[stars-shield]: https://img.shields.io/github/stars/rohit-lakhanpal/reason-over-my-data.svg?style=for-the-badge
[stars-url]: https://github.com/rohit-lakhanpal/reason-over-my-data/stargazers
[issues-shield]: https://img.shields.io/github/issues/rohit-lakhanpal/reason-over-my-data.svg?style=for-the-badge
[issues-url]: https://github.com/rohit-lakhanpal/reason-over-my-data/issues
[license-shield]: https://img.shields.io/github/license/rohit-lakhanpal/reason-over-my-data.svg?style=for-the-badge
[license-url]: https://github.com/rohit-lakhanpal/reason-over-my-data/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/rohitlakhanpal


[openai.com]: https://img.shields.io/badge/OpenAI-5A5AFF?style=for-the-badge&logo=openai&logoColor=white
[openai-url]: https://openai.com/
[azure.com]: https://img.shields.io/badge/Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white
[azure-url]: https://azure.microsoft.com
[dotnet.microsoft.com]: https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white
[dotnet-url]: https://dotnet.microsoft.com
[python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python-url]: https://www.python.org
[learn-sk]: https://img.shields.io/badge/Semantic%20Kernel-5E5E5E?style=for-the-badge&logo=microsoft
[sk-url]: https://learn.microsoft.com/en-us/semantic-kernel/
[llama-index-url]: https://img.shields.io/badge/Llama%20Index-5E5E5E?style=for-the-badge&logo=meta
[llama-index-site]: https://docs.llamaindex.ai/


