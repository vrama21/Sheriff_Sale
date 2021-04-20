import React, { useContext } from 'react';
import Paginate from '../Paginate/Paginate';
import Listing from '../Listing/Listing';
import Loading from '../Loading/Loading';
import { Grid } from '@material-ui/core';
import { ListingInterface } from '../../types';
import { ListingViewStyles } from './ListingView.styles';
import { AppContext } from '../../App';

interface ListingViewProps {
  listings: Record<string, undefined>[];
}

const ListingView: React.FC<ListingViewProps> = ({ listings }: ListingViewProps) => {
  const classes = ListingViewStyles();
  const { state } = useContext(AppContext);

  const { currentPage } = state;
  const listingsPerPage = 10;
  const indexOfLastBorrower = currentPage * listingsPerPage;
  const indexOfFirstBorrower = indexOfLastBorrower - listingsPerPage;
  const pageCount = listings && Math.ceil(listings.length / listingsPerPage);

  const filteredListingsView = listings
    ?.slice(indexOfFirstBorrower, indexOfLastBorrower)
    .map((listing: ListingInterface, listingIndex: number) => <Listing listing={listing} key={`${listing.address_sanitized}-${listingIndex}`} />);

  return (
    <div className={classes.root}>
      {(currentPage || currentPage > 0) && <Paginate pageCount={pageCount} />}
      {!filteredListingsView && <Loading />}
      {filteredListingsView?.length > 0 && (
        <Grid container direction="row" spacing={4}>
          <Grid item xs={12}>
            {filteredListingsView}
          </Grid>
        </Grid>
      )}
      {filteredListingsView?.length === 0 && <span>There are no results with the selected filters.</span>}
    </div>
  );
};

export default ListingView;
