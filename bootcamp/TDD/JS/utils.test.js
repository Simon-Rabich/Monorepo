import { Calculator } from './utils.js'
import assert from 'assert'
import NumberException from './NumberException.js'
import NumberVerificatorService from './verify.js'

function setUp() {
  const calc = new Calculator()
}
function test_verify_happy_path() {
  const numberVerficationService = new NumberVerificatorService()
  assert.equal(numberVerficationService.verify(6), true)
}
function test_verify_exception() {
  const numberVerficationService = new NumberVerificatorService()
  assert.equal(numberVerficationService.verify(666), false)
}
function test_sum_happy_path() {
  //arrange
  class NumberVerficationServiceMock {
    verify = () => {
      return true
    }
  }
  const calc = new Calculator(new NumberVerficationServiceMock()) //act
  const result = calc.sum(1, 2)
  //assert
  assert.equal(result, 3)
}
function test_sum_verification_error() {
  try {
    class NumberVerficationServiceMock {
      verify = () => {
        return false
      }
    }
    const calc = new Calculator(new NumberVerficationServiceMock())
    const answer = calc.sum(1, 2)
  } catch (error) {
    if (error instanceof NumberException) return true
  }
  return false
}
function test_divide_happy_path() {
  const res = Calculator.divide(4, 2)
  assert.equal(res, 2)
}
function test_divide_bad_res() {
  const res = Calculator.divide(2, 4)
  assert.equal(res, 0.5) //oops for js
}
function test_divide_by_zero() {
  const res = Calculator.divide(4, 0)
  if (res == Infinity) return true
  else return false
}
test_verify_happy_path()
test_verify_exception()
test_sum_happy_path()
test_sum_verification_error()
test_divide_happy_path()
test_divide_bad_res()
test_divide_by_zero()

//Component test
function test_sum_beast_numbers() {
  const calc = new Calculator()
  try {
    const res = calc.sum(1, 666)
  } catch (error) {
    if (error instanceof NumberException) return true
  }
  return false
}
const a = test_sum_beast_numbers()
console.log(a)
