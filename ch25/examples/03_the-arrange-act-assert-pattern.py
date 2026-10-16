def test_average_happy_path():
    # Arrange
    numbers = [2, 4, 6]

    # Act
    result = average(numbers)

    # Assert
    assert result == 4
