# Creativity

# C-2.25 Already completed in Ch2-Reinforcement.py

# C-2.26
class ReversedSequenceIterator:
  """An iterator for any of Python's sequence types."""

  def __init__(self, sequence):
    """Create an iterator for the given sequence."""
    self._seq = sequence          # keep a reference to the underlying data
    self._k = len(sequence)       # will decrement to n-1 on first call to next

  def __next__(self):
    """Return the previous element, or else raise StopIteration error."""
    self._k -= 1                  # "advance" to next index
    if self._k > -1:
      return(self._seq[self._k])  # return the data element
    else:
      raise StopIteration()       # there are no more elements

  def __iter__(self):
    """By convention, an iterator must return itself as an iterator."""
    return self
