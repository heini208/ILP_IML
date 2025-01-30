max_vars(5).
max_body(3).

head_pred(raisin_type,1).

body_pred(low_Area,1).
body_pred(medium_Area,1).
body_pred(high_Area,1).
body_pred(low_MajorAxisLength,1).
body_pred(medium_MajorAxisLength,1).
body_pred(high_MajorAxisLength,1).
body_pred(low_MinorAxisLength,1).
body_pred(medium_MinorAxisLength,1).
body_pred(high_MinorAxisLength,1).
body_pred(low_Eccentricity,1).
body_pred(medium_Eccentricity,1).
body_pred(high_Eccentricity,1).
body_pred(low_ConvexArea,1).
body_pred(medium_ConvexArea,1).
body_pred(high_ConvexArea,1).
body_pred(low_Extent,1).
body_pred(medium_Extent,1).
body_pred(high_Extent,1).
body_pred(low_Perimeter,1).
body_pred(medium_Perimeter,1).
body_pred(high_Perimeter,1).

% Category Constraints
:- low_Area, medium_Area.
:- low_Area, high_Area.
:- medium_Area, high_Area.
:- low_MajorAxisLength, medium_MajorAxisLength.
:- low_MajorAxisLength, high_MajorAxisLength.
:- medium_MajorAxisLength, high_MajorAxisLength.
:- low_MinorAxisLength, medium_MinorAxisLength.
:- low_MinorAxisLength, high_MinorAxisLength.
:- medium_MinorAxisLength, high_MinorAxisLength.
:- low_Eccentricity, medium_Eccentricity.
:- low_Eccentricity, high_Eccentricity.
:- medium_Eccentricity, high_Eccentricity.
:- low_ConvexArea, medium_ConvexArea.
:- low_ConvexArea, high_ConvexArea.
:- medium_ConvexArea, high_ConvexArea.
:- low_Extent, medium_Extent.
:- low_Extent, high_Extent.
:- medium_Extent, high_Extent.
:- low_Perimeter, medium_Perimeter.
:- low_Perimeter, high_Perimeter.
:- medium_Perimeter, high_Perimeter.

% Direction of predicates
direction(raisin_type,(in,)).
direction(applicant,(in,)).
direction(low_Area,(in,)).
direction(medium_Area,(in,)).
direction(high_Area,(in,)).
direction(low_MajorAxisLength,(in,)).
direction(medium_MajorAxisLength,(in,)).
direction(high_MajorAxisLength,(in,)).
direction(low_MinorAxisLength,(in,)).
direction(medium_MinorAxisLength,(in,)).
direction(high_MinorAxisLength,(in,)).
direction(low_Eccentricity,(in,)).
direction(medium_Eccentricity,(in,)).
direction(high_Eccentricity,(in,)).
direction(low_ConvexArea,(in,)).
direction(medium_ConvexArea,(in,)).
direction(high_ConvexArea,(in,)).
direction(low_Extent,(in,)).
direction(medium_Extent,(in,)).
direction(high_Extent,(in,)).
direction(low_Perimeter,(in,)).
direction(medium_Perimeter,(in,)).
direction(high_Perimeter,(in,)).

% Type definitions
type(raisin_type,(applicant,)).
type(applicant,(applicant,)).
type(low_Area,(applicant,)).
type(medium_Area,(applicant,)).
type(high_Area,(applicant,)).
type(low_MajorAxisLength,(applicant,)).
type(medium_MajorAxisLength,(applicant,)).
type(high_MajorAxisLength,(applicant,)).
type(low_MinorAxisLength,(applicant,)).
type(medium_MinorAxisLength,(applicant,)).
type(high_MinorAxisLength,(applicant,)).
type(low_Eccentricity,(applicant,)).
type(medium_Eccentricity,(applicant,)).
type(high_Eccentricity,(applicant,)).
type(low_ConvexArea,(applicant,)).
type(medium_ConvexArea,(applicant,)).
type(high_ConvexArea,(applicant,)).
type(low_Extent,(applicant,)).
type(medium_Extent,(applicant,)).
type(high_Extent,(applicant,)).
type(low_Perimeter,(applicant,)).
type(medium_Perimeter,(applicant,)).
type(high_Perimeter,(applicant,)).
