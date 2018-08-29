# Ready Code Test

See instructions at https://gist.github.com/aparrish/691b0301f6737d65b01db9920a60a0a5

Written using Flask and Python 3.7.0

Endpoint: https://ready-code-test.herokuapp.com/count

## Comments

I enjoyed messing with Python having never written it before (maybe in college :thinking:).

I interpreted one of the requirements: `All responses should include a Content-Type header appropriate to the data in the response (i.e., application/json)` to mean all repsonses from `/count` and left the Flask HTML repsonses for generic issues like 404's.

The test case in [gist](https://gist.github.com/aparrish/691b0301f6737d65b01db9920a60a0a5#file-apitest-py-L18) requiring sorted result could probably be changed to make order irrelevant. Probably makes more sense to use something like [`assert.assertCountEqual()`](https://docs.python.org/3.2/library/unittest.html#unittest.TestCase.assertCountEqual) rather than forcing a server side sort without reason.

If this were a production endpoint I would have loaded the csv file into a sqlite database since the data is static and leveraging SQL would be ideal. Loading the file into memory per request isn't ideal, but was quick for test purposes.
