from src.exception import CustomException
import sys

try:
    a = 1/0
except Exception as e:
    raise CustomException(e, sys)