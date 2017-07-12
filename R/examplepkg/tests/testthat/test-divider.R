
context ("testing the divider")

test_that("testing the divider", {
  expect_equal(divider(1,1), 1)
  expect_equal(divider(2,2), 1)


  expect_equal(divider(3, 3), 1)
  

  

  expect_true(is.na(divider(3,0)))
})
