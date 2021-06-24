## Meeting Minute Generation

### Tested on

- Ubuntu 20.04
- Python 3.7

### Install Requirements

```
$ cd Backend
$ pip install -r requirements.txt 

$ wget -c https://objectstorage.ap-mumbai-1.oraclecloud.com/p/8cK15SZ-mySY2t5kymeO8WVGyDxncLEthJqip4nJGKJXNJMgdDdWn6ohkxMlrxjH/n/bm7noglpf2jq/b/FYP-Data/o/en-70k-0.2.lm.gz -O resources/en-70k-0.2.lm.gz

$ zcat resources/en-70k-0.2.lm.gz > resources/en-70k-0.2.lm

$ wget -c https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz -O resources/GoogleNews-vectors-negative300.bin.gz
```
<hr/>

## Usage
  
1. Configure AWS CLI:

    * [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html)

    ```
    $ aws configure
        AWS Access Key ID: ****************
        AWS Secret Access Key: ****************
        Default region name: ap-southeast-1
        Default output format: json
    ```

2. Serve Backend Locally:

    ```
    $ cd Backend
    $ python serve.py
    ```

    - Serve at: [http://localhost:5000](http://localhost:5000)
    - API doc: [https://documenter.getpostman.com/view/5662193/TzecDR7B](https://documenter.getpostman.com/view/5662193/TzecDR7B)

    <br/>

2. Serve Frontend Locally:

    ```
    $ cd Frontend
    $ npm install
    $ npm start
    ```

    - Serve at: [http://localhost:3000](http://localhost:3000)
