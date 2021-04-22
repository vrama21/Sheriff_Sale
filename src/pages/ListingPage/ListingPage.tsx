import React, { useContext, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Button } from '@material-ui/core';

import { AppContext } from 'App';
import { getListing } from 'actions/actions';
import { URLParams } from 'types';

import Listing from 'components/Listing/Listing';

const ListingPage: React.FC = () => {
  const { state, dispatch } = useContext(AppContext);
  const { listingId }: URLParams = useParams();

  const listingRetrieved = state.getListingSucceeded === true;
  const listing = state.data.listing;

  useEffect(() => {
    if (!listingRetrieved) {
      getListing({ listingId, dispatch });
    }
  }, [dispatch, getListing, listingId, listingRetrieved]);

  return (
    <div>
      <Link to="/">
        <Button>HOME</Button>
      </Link>

      {listing && <Listing listing={listing} />}
    </div>
  );
};

export default ListingPage;
