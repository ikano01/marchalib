import numpy as np
from astropy import wcs

def wcs2D(hdr):
    w = wcs.WCS(naxis=2)
    w.wcs.crpix = [hdr['CRPIX1'], hdr['CRPIX2']]
    w.wcs.cdelt = np.array([hdr['CDELT1'], hdr['CDELT2']])
    w.wcs.crval = [hdr['CRVAL1'], hdr['CRVAL2']]
    w.wcs.ctype = [hdr['CTYPE1'], hdr['CTYPE2']]
    return w

def set_wcs(patch_size, projx, projy, cdelt, GLON, GLAT):
    w           = wcs.WCS(naxis=2)
    w.wcs.crpix = [patch_size/2, patch_size/2]
    w.wcs.crval = [GLON, GLAT]
    w.wcs.cdelt = np.array([-cdelt,cdelt])
    w.wcs.ctype = [projx, projy]
    return w

