
import pytest
from stuff.accum import Accumulator


# Tests here using the pattern:
#  Arrange - assests
#  Act - exercise target behavior
#  Assert - results

# Fixtures accum and accum 2 moved to conftest.py

# This function now becomes a generator. 
# Anything before the yield will be setup steps
@pytest.fixture
def accum3():
    print("Before!")
    yield Accumulator()   
    print("After!")

# To run the fixture 1 time for the entire testsuite add scope
# if included will run for the first test and that's it
@pytest.fixture
def accum4(scope="session"):
  return Accumulator()  


# -------------------------------
# Tests
# ------------------------------- 
 
# Fixture added as a parameter
# an example of dependency injection

@pytest.mark.accumulator            # added a mark accumulator  
def test_accumulator_inti(accum2):   
    assert accum2.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):  
  accum.add()
  assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):  
  accum.add(3)
  assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):  
  accum.add()
  accum.add()
  assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):  
  with pytest.raises(AttributeError, match=r"can't set attribute") as e:
    accum.count = 10