import React from 'react';
import PropTypes from 'prop-types';

import { getRepoUrl } from '../../helpers/url';

export default function ReposMenu(props) {
  const { groupedRepos } = props;

  return (
    <span>
      <span className="dropdown">
        <button
          id="repoLabel"
          title="Watch a repo"
          data-toggle="dropdown"
          className="btn btn-view-nav nav-menu-btn dropdown-toggle"
        >Repos</button>
        <span
          id="repo-dropdown"
          className="dropdown-menu nav-dropdown-menu-right container"
        >
          <ul
            className="checkbox-dropdown-menu row"
            role="menu"
            aria-labelledby="repoLabel"
            aria-haspopup="true"
            aria-expanded="false"
          >
            {groupedRepos.map(group => (
              <span className="repogroup dropdown-item col" key={group.name}>
                <li
                  role="presentation"
                  className="dropdown-header"
                  title={group.name}
                >{group.name} <span className="fa fa-info-circle" /></li>
                {!!group.repos && group.repos.map(repo => (
                  <li key={repo.name}>
                    <a
                      title="Open repo"
                      className="dropdown-link"
                      href={getRepoUrl(repo.name)}
                    >{repo.name}</a>
                  </li>
                ))}
              </span>
            ))}
          </ul>
        </span>
      </span>
    </span>
  );
}


ReposMenu.propTypes = {
  groupedRepos: PropTypes.array.isRequired,
};
