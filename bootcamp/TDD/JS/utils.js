import NumberVerificatorService from './verify.js'
import NumberException from '../NumberException.js'

export class Calculator {
  constructor(numberVerificatorService = new NumberVerificatorService()) {
    this.numberVerificatorService = numberVerificatorService
  }
  
  sum(a, b) {
    this.#verifyNumber(a, b)
    return a + b
  }

  #verifyNumber(a, b) {
    Object.values(arguments).forEach((value) => {
      if (!this.numberVerificatorService.verify(value))
        throw new NumberException('number Is Not Verified')
    })
  }

  static divide(a, b) {
    return a / b
  }
}
