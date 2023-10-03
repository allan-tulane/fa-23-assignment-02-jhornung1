from main import subquadratic_multiply, BinaryNumber


## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(0), BinaryNumber(2)) == 0*2
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(2)) == 4*2
    assert subquadratic_multiply(BinaryNumber(100), BinaryNumber(2)) == 100*2
    assert subquadratic_multiply(BinaryNumber(10202), BinaryNumber(2)) == 10202*2