# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC x=10
# MAGIC 
# MAGIC if x > 5:
# MAGIC   raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# COMMAND ----------

def qux(): 
    try: 
        fun() 
    except Exception as exc: 
        raise RuntimeError('Qux') from exc 
                                                                                                  

def fun(): 
    raise ValueError('Foo bar baz') 
    
    
qux()

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install --upgrade pip

# COMMAND ----------

# MAGIC %sh
# MAGIC pip install ipython==2.2.0

# COMMAND ----------

# MAGIC %python
# MAGIC 
# MAGIC x=10
# MAGIC 
# MAGIC if x > 5:
# MAGIC   raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# COMMAND ----------

