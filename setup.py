from setuptools import setup, find_packages

setup(
  name = 'swarms',
  packages = find_packages(exclude=[]),
  version = '1.3.0',
  license='MIT',
  description = 'Swarms - Pytorch',
  author = 'Kye Gomez',
  author_email = 'kye@apac.ai',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/kyegomez/swarms',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'optimizers',
    "Prompt Engineering"
  ],
  install_requires=[
        'transformers',
        'openai',
        'langchain==0.0.240',
        # 'torch',
        # 'torchvision',
        # 'torchaudio',
        'asyncio',
        'nest_asyncio',
        'pegasusx',
        'google-generativeai',
        'oceandb',
        'langchain-experimental',
        # 'codeinterpreterapi',
        'playwright',
        'duckduckgo_search',
        'faiss-cpu',
        'wget==3.2',
        # 'addict',
        # 'albumentations',
        # 'basicsr',
        # 'controlnet-aux',
        # 'diffusers',
        # 'einops',
        # 'imageio',
        'simpleaichat',
        # 'kornia',
        # 'numpy',
        # 'omegaconf',
        # 'open_clip_torch',
        # 'opencv-python',
        # 'prettytable',
        # 'safetensors',
        # 'test-tube',
        # 'timm',
        # 'torchmetrics',
        # 'webdataset',
        # 'yapf',
        'httpx',
        'ggl',
        'beautifulsoup4',
        # 'llama-index',
        'fastapi',
        'pydantic',
        'tenacity',
        # 'python-dotenv',
        # 'boto3',
        # 'jinja2',
        'python-multipart==0.0.6',
        'celery',
        'redis',
        'psycopg2-binary==2.9.5',
        'google-search-results==2.4.2',
        'Pillow',
        # 'selenium',
        # # 'controlnet_aux',
        # 'espnet==202301',
        # 'espnet_model_zoo==0.1.7',
        # 'waitress==2.1.2',
        # # 'asteroid',
        # 'typeguard',
        # 'pytesseract',
        # 'fastapi-cache',
        # 'fastapi-limiter',
    ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)