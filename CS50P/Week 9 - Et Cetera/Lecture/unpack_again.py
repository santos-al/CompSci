def f(*args, **kwargs):
  print("Postional: ", args)
  print("Named: ", kwargs)

f(galleons=100, sickles=50, knuts=30)