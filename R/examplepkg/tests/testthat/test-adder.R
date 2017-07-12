context("testing the adder")

test_that("testing the adder", {
  expect_equal(add(1,1), 2)
  expect_equal(add(1,2), 3)

})

