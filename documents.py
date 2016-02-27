words = {'has':['had', 'has', 'will have']}

class Message:
    """Message class."""


class Measurement:
    """Measurement class."""

    def __init__(self, unit, number):
        self.unit = unit
        self.number = number


class Specification:
    """Specification class."""


class RelativeVariation(Specification):
    """RelativeVariation class."""

    def __init__(self, direction, magnitude):
        self.direction = direction
        self.magnitude = magnitude


class AbsoluteSpec(Specification):
    """AbsoluteSpec class."""

    def __init__(self, amount):
        self.amount = amount


class DocumentPlan:
    """DocumentPlan class."""

    def __init__(self, children):
        self.children = children


class Constituents:
    """Constituents class."""


class NSConstituents(Constituents):
    """A nucleus and its rhetorical satellites."""

    def __init__(self, nucleus, satellites):
        """nucleus - DocumentPlan or Message
           satellites - list of SatelliteSpec

        """
        self.nucleus = nucleus
        self.satellites = satellites


class SatelliteSpec:
    """A satellite and its rhetorical relation to the nucleus."""

    def __init__(self, relation, satellite):
        """relation - DiscourseRelation
           satellite - DocumentPlan or Message

        """
        self.relation = relation
        self.satellite = satellite


class ConstituentSet(Constituents):
    """A set of constituents without a nucleus."""

    def __init__(self, relation, constituents):
        """relation - DiscourseRelation
           constituents - list of DocumentPlan or Message

        """
        self.relation = relation
        self.constituents = constituents


class DPDocument(DocumentPlan):
    """Document plan for complete document."""

    def __init__(self, children, title):
        """title - Message or PhraseSpec

        """
        super(DPDocument, self).__init__(children)
        self.title = title


class DPParagraph(DocumentPlan):
    """Document plan for paragraph."""

    def __init__(self, children):
        super(DPParagraph, self).__init__(children)


def document_planner(k, c, u, d):
    """k - knowledge source
       c - communicative goal
       u - user model (ex: farmers vs mariners pg45)
       d - discourse history

    """
    pass

