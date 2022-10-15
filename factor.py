from collections import defaultdict


class Factor:
    """A factor in a Bayesian network (i.e. a multivariable function)"""

    def __init__(self, variables, values):
        """
        Parameters
        ----------
        variables : list[str]
            The variables of the factor
        values : dict[tuple[str], float]
            A dictionary mapping each event (expressed as a tuple) to its value
        """

        self._variables = variables
        self._values = values
    
    def get_variables(self):
        """Returns the variables of the factor.

        Returns
        -------
        list[Variable]
            The variables of the factor.
        """

        return self._variables

    def get_value(self, event):
        """Returns the value that the factor assigns to a particular event.

        Returns
        -------
        float
            The value associated with the event

        Raises
        ------
        KeyError
            If the factor has no value assigned to the given event.
        """

        key = []
        for var in self._variables:
            if var not in event:
                raise KeyError(f'Variable {var} not found in given event.')
            key.append(event[var])
        if tuple(key) in self._values:
            return self._values[tuple(key)]
        else:
            raise KeyError(f'No value assigned to event {event}.')

    def normalize(self):
        """Normalizes the event values.

        In other words, each event value is divided by the overall sum of the event
        values so that they all sum to one.

        Returns
        -------
        Factor
            A new Factor, identical to the current Factor, except that the event values
            are normalized.
        """
        ... # question two

    def reduce(self, evidence):
        """Removes any events in the factor that do not agree with the "evidence" event.

        An event "does not agree" with another event if the two events associate different
        domain values with some variable. For instance, the following events agree:
            {'P': 'yes', 'D': 's', 'R': '+'}
            {'P': 'yes', 'D': 's', 'T': '-'}
        because there is no variable associated with different values in the two events.
        However:
            {'P': 'yes', 'D': 'n', 'R': '+'}
            {'P': 'yes', 'D': 's', 'T': '-'}
        do not agree, since the variable 'D' is associated with different values in the
        events.

        Parameters
        ----------
        evidence : dict[str, str]
            The "evidence" event.

        Returns
        -------
        Factor
            A new Factor, identical to the current Factor, except that events that disagree
            with the evidence event are removed.
        """
        ... # question two

    def marginalize(self, variable):
        """Marginalizes (sums) out the specified variable.

        Parameters
        ----------
        variable : Variable
            The variable to marginalize out.

        Returns
        -------
        Factor
            A new Factor, identical to the current Factor with the specified variable
            marginalized out.
        """
        ... # question two

    def __str__(self):
        result = f"{self._variables}:"
        for event, value in self._values.items():
            result += f"\n  {event}: {value}"
        return result

    __repr__ = __str__


def events(vars, domains):
    """
    Takes a list of variables and returns the cross-product of the domains.

    For instance, suppose the domain of variable X is ('a', 'b') and the
    domain of the variable Y is ('c','d','e'). Then:

       >>> X = Variable('X', ('a', 'b'))
       >>> Y = Variable('Y', ('c', 'd', 'e'))
       >>> events([X, Y])
       [('a', 'c'), ('a', 'd'), ('a', 'e'), ('b', 'c'), ('b', 'd'), ('b', 'e')]
    """
    ... # question one


def multiply_factors(factors, domains):
    """Multiplies a list of factors.

    Parameters
    ----------
    factors : list[Factor]
        The factors to multiply
    domains : dict[str, list[str]]
        A dictionary mapping each variable to its possible values

    Returns
    -------
    Factor
        The product of the input factors.
    """
    ... # question three


