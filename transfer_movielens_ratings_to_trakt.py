#!/usr/bin/env python
import transfer_ratings


def main():
    transfer_ratings.main([__file__, 'movielens', 'trakt'])

if __name__ == "__main__":
    main()
