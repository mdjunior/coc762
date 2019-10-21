# Processamento Intensivo de dados

Esse repositório contempla os códigos utilizados na disciplina COC762 da COPPE/UFRJ que aborda Processamento Intensivo de Dados. A disponibilização do código aqui presente tem o objetivo de facilitar futuras consultas nessa área, assim como auxiliar futuros estudantes da disciplina.

## Trabalho inicial

A disciplina de Processamento Intensivo de dados possui um trabalho inicial que deve ser desenvolvido ao longo do curso. O objetivo do mesmo é ser um trabalho investigativo sobre as tecnologias utilizadas relacionadas com o tema.


## Trabalho final

A disciplina também contempla um trabalho final, cujo os arquivos estão disponíveis nesse repositório. O trabalho final foi realizado utilizando uma imagem Docker e o procedimento para reprodução dos passos está a seguir.

### Geração dos dados

Para gerar os dados, crie um sistema isolado (como uma VM na Amazon e copie o arquivo `generate.py`). Feito isso, execute o comando a seguir:

```
sudo yum install -y python36 python36-pip
sudo pip3 install cryptography
```

Dessa forma, as dependências serão instaladas no sistema. Você pode iniciar uma sessão do [tmux](https://github.com/tmux/tmux/wiki) antes para continuar utilizando o terminal, caso esteja em uma VM. Para iniciar a geração de dados, execute:

```
time python3 generate.py
```

Ao término, você terá o tempo de CPU utilizado para a geração dos dados. Caso seja do seu interesse, você poderá enviar os dados para um bucket no S3, executando:

```
aws s3 sync . s3://<seu bucket>
```

### Execução da análise com Spark

Com os dados gerados, você pode fazer a execução dos dados utilizando Spark. Para esse trabalho, um containner Docker foi utilizado. Para repetir o procedimento, você pode fazer:

```
docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```

Após a inicialização, você pode fazer upload do arquivo `Aleatoriedade em curvas elípticas.ipynb` e realizar a análise.

### Execução utilizando o HDFS e MapReduce

Arquivos `.java` são fornecidos para execução através dos arquivos caso eles sejam copiados no HDFS.