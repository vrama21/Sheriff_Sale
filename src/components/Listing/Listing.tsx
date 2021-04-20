import React from 'react';
import { Grid, Typography } from '@material-ui/core';
import ListingMap from '../ListingMap/ListingMap';
import { listingStyles } from './Listing.style';
import { ListingInterface } from '../../types';
import { formatToCurrency } from '../../helpers/formatToCurrency';
import googleMapsIcon from '../../assets/google-maps-icon.png';

const Listing: React.FC<ListingInterface> = ({
  address,
  attorney,
  attorney_phone,
  city,
  defendant,
  judgment,
  maps_url,
  latitude,
  longitude,
  plaintiff,
  priors,
  sale_date,
  state,
  street,
  upset_amount,
  zip_code,
}: ListingInterface) => {
  const classes = listingStyles();
  const formattedAddress = city && street && `${street}, ${city}, ${state} ${zip_code}`;

  return (
    <div className={classes.root}>
      <div className={classes.addressHeader}>
        {formattedAddress || address}
        {maps_url && (
          <a href={maps_url} target="_blank">
            <img className={classes.googleMapsLogo} src={googleMapsIcon} />
          </a>
        )}
      </div>

      <Grid container className={classes.listingContainer}>
        <Grid item xs={4}>
          {latitude && longitude && <ListingMap latitude={latitude} longitude={longitude} />}
        </Grid>
        <Grid item xs={2}>
          <span className={classes.listingLabel}>Sale Date: </span>
          {judgment && <span className={classes.listingLabel}>Judgment: </span>}
          {upset_amount && <span className={classes.listingLabel}>Upset Amount: </span>}
          {priors && <span className={classes.listingLabel}>Priors: </span>}
        </Grid>
        <Grid item xs={2}>
          <span className={classes.listingValue}>{sale_date}</span>
          {judgment && <span className={classes.listingValue}>{formatToCurrency(judgment)}</span>}
          {upset_amount && <span className={classes.listingValue}>{formatToCurrency(upset_amount)}</span>}
          <span className={classes.listingValue}>{priors}</span>
        </Grid>
        <Grid item xs={2}>
          <span className={classes.listingLabel}>Attorney: </span>
          {attorney_phone && <span className={classes.listingLabel}>Attorney Phone: </span>}
          <span className={classes.listingLabel}>Plaintiff: </span>
          <span className={classes.listingLabel}>Defendant: </span>
        </Grid>
        <Grid item xs={2}>
          <Typography noWrap className={classes.listingValue}>
            {attorney}
          </Typography>
          {attorney_phone && <span className={classes.listingValue}>{attorney_phone}</span>}
          <Typography noWrap className={classes.listingValue}>
            {plaintiff}
          </Typography>
          <Typography noWrap className={classes.listingValue}>
            {defendant}
          </Typography>
        </Grid>
      </Grid>
    </div>
  );
};

export default Listing;
